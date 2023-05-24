"""对招聘信息的薪资进行分析"""

import os
import pandas
import re
from tqdm import tqdm
import copy
import pickle
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']

""""获取不同城市的薪资情况"""
city=['全国','北京','上海','深圳','其它']
edu=['1年以内','1-3','3-5','5-10']
stu=['本科以下','本科','本科以上']

def get_city_salary():
    sal = dict()
    for x in city:
        ct = dict()
        for z in stu:
            cg=dict()
            for y in edu:
                cg[y] = []
            ct[z]=cg
        sal[x] = ct
    job_salary=dict()
    data=pandas.read_csv('File/Boss_jobitem.csv')
    for i in range(len(data)):
        jobname=data['Type'][i]
        area=data['job_area'][i].split('·')[0]
        ye=data['year'][i]
        edx=data['education'][i]
        sal_top=data['salary-top'][i]
        sal_bot=data['salary-bot'][i]
        sal_av=(sal_bot+sal_top)/2
        if (jobname not in job_salary.keys()):
            job_salary[jobname]=copy.deepcopy(sal)
        if(area in city):
            if(edx=='本科'):
                if(ye in edu):
                    job_salary[jobname][area][edx][ye].append(sal_av)
                elif (ye == '在校'):
                    job_salary[jobname][area][edx]['1年以内'].append(sal_av)
                else:
                    for vb in edu:
                        job_salary[jobname][area][edx][vb].append(sal_av)
            elif(edx=='硕士' or edx=='博士'):
                if (ye in edu):
                    job_salary[jobname][area]['本科以上'][ye].append(sal_av)
                elif (ye == '在校'):
                    job_salary[jobname][area]['本科以上']['1年以内'].append(sal_av)
                else:
                    for vb in edu:
                        job_salary[jobname][area]['本科以上'][vb].append(sal_av)
            elif(edx=='中专' or edx=='大专'):
                if (ye in edu):
                    job_salary[jobname][area]['本科以下'][ye].append(sal_av)
                elif (ye == '在校'):
                    job_salary[jobname][area]['本科以下']['1年以内'].append(sal_av)
                else:
                    for vb in edu:
                        job_salary[jobname][area]['本科以下'][vb].append(sal_av)
            else:
                for ty in stu:
                    if (ye in edu):
                        job_salary[jobname][area][ty][ye].append(sal_av)
                    elif (ye == '在校'):
                        job_salary[jobname][area][ty]['1年以内'].append(sal_av)
                    else:
                        for vb in edu:
                            job_salary[jobname][area][ty][vb].append(sal_av)
        else:
            if (edx == '本科'):
                if (ye in edu):
                    job_salary[jobname]['其它'][edx][ye].append(sal_av)
                elif (ye == '在校'):
                    job_salary[jobname]['其它'][edx]['1年以内'].append(sal_av)
                else:
                    for vb in edu:
                        job_salary[jobname]['其它'][edx][vb].append(sal_av)
            elif (edx == '硕士' or edx == '博士'):
                if (ye in edu):
                    job_salary[jobname]['其它']['本科以上'][ye].append(sal_av)
                elif (ye == '在校'):
                    job_salary[jobname]['其它']['本科以上']['1年以内'].append(sal_av)
                else:
                    for vb in edu:
                        job_salary[jobname]['其它']['本科以上'][vb].append(sal_av)
            elif (edx == '中专' or edx == '大专'):
                if (ye in edu):
                    job_salary[jobname]['其它']['本科以下'][ye].append(sal_av)
                elif (ye == '在校'):
                    job_salary[jobname]['其它']['本科以下']['1年以内'].append(sal_av)
                else:
                    for vb in edu:
                        job_salary[jobname]['其它']['本科以下'][vb].append(sal_av)
            else:
                for ty in stu:
                    if (ye in edu):
                        job_salary[jobname]['其它'][ty][ye].append(sal_av)
                    elif (ye == '在校'):
                        job_salary[jobname]['其它'][ty]['1年以内'].append(sal_av)
                    else:
                        for vb in edu:
                            job_salary[jobname]['其它'][ty][vb].append(sal_av)
        if (edx == '本科'):
            if (ye in edu):
                job_salary[jobname]['全国'][edx][ye].append(sal_av)
            elif (ye == '在校'):
                job_salary[jobname]['全国'][edx]['1年以内'].append(sal_av)
            else:
                for vb in edu:
                    job_salary[jobname]['全国'][edx][vb].append(sal_av)
        elif (edx == '硕士' or edx == '博士'):
            if (ye in edu):
                job_salary[jobname]['全国']['本科以上'][ye].append(sal_av)
            elif (ye == '在校'):
                job_salary[jobname]['全国']['本科以上']['1年以内'].append(sal_av)
            else:
                for vb in edu:
                    job_salary[jobname]['全国']['本科以上'][vb].append(sal_av)
        elif (edx == '中专' or edx == '大专'):
            if (ye in edu):
                job_salary[jobname]['全国']['本科以下'][ye].append(sal_av)
            elif (ye == '在校'):
                job_salary[jobname]['全国']['本科以下']['1年以内'].append(sal_av)
            else:
                for vb in edu:
                    job_salary[jobname]['全国']['本科以下'][vb].append(sal_av)
        else:
            for ty in stu:
                if (ye in edu):
                    job_salary[jobname]['其它'][ty][ye].append(sal_av)
                elif (ye == '在校'):
                    job_salary[jobname]['其它'][ty]['1年以内'].append(sal_av)
                else:
                    for vb in edu:
                        job_salary[jobname]['其它'][ty][vb].append(sal_av)
    for jobname in job_salary.keys():
        for ci in city:
            for sd in stu:
                for e in edu:
                    adv=0
                    i=0
                    for sal in job_salary[jobname][ci][sd][e]:
                        adv+=sal
                        i+=1
                    if(i!=0):
                        if(e=='1年以内'):
                            job_salary[jobname][ci][sd][e]=int(adv/(i*1.5))
                        else:
                            job_salary[jobname][ci][sd][e] = int(adv / i)
                    else:
                        job_salary[jobname][ci][sd][e]=0
    for jobname in job_salary.keys():
        for ci in city:
            for sd in stu:
                    print(job_salary[jobname][ci][sd])
    for jobname in tqdm(job_salary.keys()):
        for ci in city:
            for sd in stu:
                x_axis_data = edu  # x
                y_axis_data=[]
                for e in edu:
                    y_axis_data.append(job_salary[jobname][ci][sd][e])
                for x, y in zip(x_axis_data, y_axis_data):
                    plt.text(x, y + 0.5, '%.00f' % y, ha='center', va='bottom', fontsize=10)  # y_axis_data1加标签数据
                plt.plot(x_axis_data, y_axis_data, 'b*--', alpha=0.5, linewidth=1, label=jobname+'-'+ci+'-'+sd)  # 'bo-'表示蓝色实线，数据点实心原点标注
                ## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，
                plt.legend()  # 显示上面的label
                plt.xlabel('年限')  # x_label
                plt.ylabel('薪资（K/月）')  # y_label
                plt.savefig('pic/Salary/'+jobname+'-'+ci+'-'+sd+'.png')
                plt.clf()

education={"中专":0,'大专':1,'本科':2,'硕士':3,'博士':4,"学历不限":5}
def get_education():#对各职业的学历要求进行统计
    job_edu=dict()
    all=[0,0,0,0,0,0]
    data = pandas.read_csv('File/Boss_jobitem.csv')
    for i in range(len(data)):
        jobname = data['Type'][i]
        edx = data['education'][i]
        if (jobname not in job_edu.keys()):
            job_edu[jobname] = [0,0,0,0,0,0]
        if(edx in education.keys()):
            job_edu[jobname][education[edx]]+=1
            all[education[edx]]+=1
    # for jobname in job_edu.keys():
    #     plt.rcParams['font.family'] = 'SimHei'
    #     plt.rcParams['axes.unicode_minus'] = False
    #     plt.pie(job_edu[jobname], labels=["中专",'大专','本科','硕士','博士',"学历不限"],autopct='%1.1f%%',explode=[0.1,0.1,0.1,0.1,0.1,0.1],radius=1.2)
    #     plt.savefig('pic/Education/' + jobname+ '.png')
    #     plt.clf()
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.pie(all, labels=["中专",'大专','本科','硕士','博士',"学历不限"],autopct='%1.1f%%',explode=[0.1,0.1,0.1,0.1,0.1,0.1],radius=1.2)
    plt.savefig('pic/Education/all.png')
    plt.clf()
# get_city_salary()
get_education()