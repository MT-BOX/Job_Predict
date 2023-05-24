import os
import pandas
import re
from tqdm import tqdm
import copy
import pickle

"""职位地区统计"""
import requests
import json


def gain_location(address):
    AK = '5fXsjcG0yBrIVlrU0TGr5AcFGYMf8jl3'
    api_url = 'http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}&callback=showLocation'.format(address,AK)
    r = requests.get(api_url)
    r = r.text
    '''经历以下两次去除，使得最终结果为json格式的数据 
       原来的数据格式：showLocation&&showLocation(' showLocation&&showLocation('showLocation&&showLocation({"status":0,"result":{"location":{"lng":108.94646555063274,"lat":34.34726881662395},"precise":0,"confidence":12,"comprehension":63,"level":"城市"}}）
       去除后的数据格式为将json字符串转换为字典类型：showLocation&&showLocation({"status":0,"result":{"location":{"lng":108.94646555063274,"lat":34.34726881662395},"precise":0,"confidence":12,"comprehension":63,"level":"城市"}}
    '''
    r = r.strip('showLocation&&showLocation(')
    r = r.strip(')')
    jsonData = json.loads(r)  # 将json字符串转换为字典类型转为字典格式类型
    return jsonData

def getapiadd():
    # 读取xlsx文件,并使用百度接口函数将文件地名数据转为经纬度，并改成一定的格式
    filenames = os.listdir("area_txt")
    for file in tqdm(filenames):
        ws=pandas.read_csv('area_txt/'+file)
        data = open('location/' + file + '.json', 'w')
        for i in range(len(ws)):  # 遍历工作表的每一行
            line =[ws['area'][i],ws['count'][i]]
            location=gain_location(line[0])['result']['location']
            lng = location['lng']  # 提取网址返回的经度
            lat = location['lat']  # 提取网址返回的纬度
            count = line[1]  # 地名计数
            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(count) + '},\n'  # 将经度，纬度，计数变成格式
            print(str_temp)  # 打印出格式，要待会儿直接要复制打印结果到别的文件中
            data.write(str_temp)
        data.close()

def count_area():#统计职位地点信息：
    data = pandas.read_csv('File/Boss_jobitem.csv')
    area_dic = {'all':[]}

    for i in tqdm(range(len(data))):  # 分词处理
        type = data['Type'][i]
        area=data['job_area'][i].split('·')[0]
        if (type not in area_dic.keys()):
            area_dic[type] = 1
        flag=True
        for i in range(len(area_dic[type])):
              if(area_dic[type][i][0] == area):
                  area_dic[type][i][1]+=1
                  flag=False
                  break
        if(flag):
            area_dic[type].append([area,1])

    for jobname in area_dic.keys():
        area_dic[jobname].sort(key=lambda x: x[1], reverse=True)
        fieldnames = pandas.DataFrame(columns=['area', 'count'])
        for x in area_dic[jobname]:
            s = {'area':x[0], 'count':x[1]}
            fieldnames = fieldnames.append(s,ignore_index=True)
        fieldnames.to_csv('area_txt/'+jobname+'.csv', index=False)

getapiadd()