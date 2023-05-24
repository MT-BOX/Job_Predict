"""BOSS直聘网站信息爬虫
   Selenium库模拟浏览器爬取
"""
from selenium import webdriver  # 调用这个模块
from selenium.webdriver.common.keys import Keys  # 导入这个模块就是可以模拟键盘操作
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
import csv
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
import pandas


with open("File/职业.txt", "r",encoding='utf_8_sig') as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
job_list=data.split('\n')

browser = webdriver.Firefox()

#新建CSV文件
def newcsv(workname):
    fieldnames = pandas.DataFrame(columns=['Type','job_title', 'job_area','salary', 'condition', 'company_title', 'company_info','skill',
                 'publis_name','welfare','job_url'],dtype='str')
    fieldnames['Type'] = ''           #职业名称
    fieldnames['job_title']=''        #岗位名称
    fieldnames['job_area'] = ''       #岗位地区
    fieldnames['salary'] = ''         #薪酬
    fieldnames['condition'] = ''      #岗位情况
    fieldnames['company_title'] = ''  #公司名称
    fieldnames['company_info'] = ''   #公司情况
    fieldnames['skill'] = ''          #岗位技能
    fieldnames['publis_name'] = ''    #招聘人
    fieldnames['welfare'] = ''        #福利情况
    fieldnames['job_url'] = ''        #招聘链接
    return fieldnames

#根据职业和页面去爬取
def inquire_job(browser, job_name,page):
    # 输入需要查询的职位
    url="https://www.zhipin.com/job_detail/?query="+job_name+"&page="+str(page)+"&city=100010000"
    browser.get(url)

#分析页面并保存
def get_job_items(job_list,fieldnames,workname):

    for item in job_list:
        ast=str(item.text).split('\n')
        print(ast)
        result = {}
        job = item.find_element(by=By.CLASS_NAME,value='info-primary')
        if(len(ast)<9):
            ast.append(' ')
        s = {'Type':workname,'job_title':ast[0], 'job_area':ast[1],'salary':ast[2], 'condition':ast[3], 'company_title':ast[5], 'company_info':ast[6],'skill':ast[7],
             'publis_name':ast[4],'welfare':ast[8],'job_url':job.find_element(by=By.CSS_SELECTOR, value='a').get_attribute('href')}
        fieldnames=fieldnames.append(s,ignore_index=True)
    return fieldnames
#遍历职业列表
print(job_list)
for workname in job_list:
    fieldnames=newcsv(workname)
    for i in range(1,11):     #爬取10页的招聘信息
        try:
            inquire_job(browser,workname,i)
            time.sleep(30)
            job_list = browser.find_elements(by=By.XPATH, value="//div[@class='job-list']//li")
            if (len(job_list) == 0):
                break
            fieldnames=get_job_items(job_list,fieldnames,workname)
        except:
            print("Error!!!")
    time.sleep(100)
    fieldnames.to_csv("Job_csv/"+workname+"_job_items.csv", encoding='utf_8_sig', index=False)
#单个职业写入文件

browser.close()