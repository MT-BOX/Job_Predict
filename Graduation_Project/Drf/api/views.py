from django .shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from model import Score_model
import pickle
import copy
import pandas
import Data_cs

newone={'name':'','key':'','sex':'','age':'','skill':[],'education':'','phone':'','email':''}

"""登录接口"""
class Loginview (APIView) :
    def post (self,request,*args ,**kwargs):
        print(request.data)
        account = pandas.read_pickle('file/account.pickle')
        if(request.data['username'] in account.keys()):
            if(request.data['password']==account[request.data['username']]['key']):
                return Response ({"isok":1 ,"account":account[request.data['username']]})
            else:
                return Response ({"isok":3})
        else:
            return Response({"isok": 2})

"""创建新账号接口"""
class Creatview (APIView) :
    def post(self,request,*args ,**kwargs):
        account = pandas.read_pickle('file/account.pickle')
        account[request.data['username']]=copy.deepcopy(newone)
        account[request.data['username']]['phone']=request.data['username']
        account[request.data['username']]['key']=request.data['password']
        pickle.dump(account, open('file/account.pickle', 'wb'))
        return Response({"account": account[request.data['username']]})


"""修改资料接口"""
class Correctview(APIView) :
    def post(self,request,*args ,**kwargs):
        account = pandas.read_pickle('file/account.pickle')
        print(request.data)
        account[request.data['phone']]['name']=request.data['name']
        account[request.data['phone']]['sex'] = request.data['sex']
        account[request.data['phone']]['age'] = request.data['age']
        account[request.data['phone']]['email'] = request.data['email']
        account[request.data['phone']]['education'] = request.data['education']
        pickle.dump(account, open('file/account.pickle', 'wb'))
        return Response({"isok": True})

"""修改密码接口"""
class Ckeyview(APIView) :
    def post(self,request,*args ,**kwargs):
        account = pandas.read_pickle('file/account.pickle')
        account[request.data['username']]['key']=request.data['password']
        pickle.dump(account, open('file/account.pickle', 'wb'))
        return Response({"isok": True})

"""获取skill"""
class Getskillview(APIView) :
    def post(self,request,*args ,**kwargs):
        skills=pandas.read_pickle('file/skill_choice.pickle')
        return Response({"skill": skills})

"""预测结果接口"""
class Predictview(APIView) :
    def post(self,request,*args ,**kwargs):
        account = pandas.read_pickle('file/account.pickle')
        skills=request.data['skills'].split(',')
        print(skills)
        account[request.data['account']]['skill']=skills
        pickle.dump(account, open('file/account.pickle', 'wb'))
        model = Score_model()
        result = model.predict(skills)
        print(result)
        return Response({"result": result})

class Getmessview(APIView) :
    def post(self,request,*args ,**kwargs):
        job_bri=pandas.read_pickle('file/job_briefly.pickle')
        skills=request.data['skill'].split(',')
        jobname=request.data['jobname']
        education = request.data['education']
        welfare=request.data['welfare']
        joblist=Data_cs.getcomjob(jobname,skills,education,welfare)
        jobexe=Data_cs.getskills(jobname,skills)
        return Response({"job_bri": job_bri[jobname],'joblist':joblist,'jobexe':jobexe})
# Create your views here.
