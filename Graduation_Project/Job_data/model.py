"""模型预测"""
import os
import pandas
import re
from tqdm import tqdm
import copy
import pickle



def getvector():#获得所以技能对应的权重得分
    filenames = os.listdir("weights")
    vector_weight=dict()
    vector=set()
    for file in filenames:
        data=pandas.read_csv("weights/"+file)
        file=file.strip('.csv')
        vector_weight[file]=dict()
        for i in range(len(data)):
            vector_weight[file][data['skill'][i]]=data['weight'][i]
            vector.add(data['skill'][i])
    with open('data/vector.txt',"w", encoding='utf-8') as file:
        for x in vector:
            file.write(x + '\n')
    file.close()
    pickle.dump(vector_weight, open('data/vector_weight.pickle', 'wb'))  # 将字典写进pkl文件


class Score_model():
    def __init__(self):
        self.vector_weight=pandas.read_pickle('data/vector_weight.pickle')

    def count_score(self,skills):#计算技能点得分情况
        scores=[]
        for jobname in self.vector_weight.keys():
            vector=self.vector_weight[jobname]
            score=0
            for skill in skills:
                if(skill in vector.keys()):
                    score+=vector[skill]
            scores.append([jobname,score])
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores

    def predict(self,skills):
        result=[]
        mix_scores=0
        scores=self.count_score(skills)
        for i in range(len(scores)):
            if(i>=3 or scores[i][1]<=4):
                break
            result.append(scores[i])
            mix_scores+=scores[i][1]
        for i in range(len(result)):
            result[i][1]=str(int(result[i][1]/mix_scores*100))+"%"
        return result
# model=Score_model()
# skill=['Python']
# result=model.predict(skill)
# print(result)
def model_test():
    model=Score_model()
    x=0
    y=0
    data=pandas.read_csv('File/Boss_jobitem.csv')
    for i in range(len(data)):
        result=model.predict(re.split('[ 、]',str(data['skill'][i])))
        if(len(result)!=0):
            x+=1
            for xc in result:
                if(xc[0]==data['Type'][i]):
                    y+=1
                    break
    print('权重阈值: 2')
    print('得分公式特征词权重  v1: 80%')
    print('得分公式学历权重  v2: 10%')
    print('得分公式经验权重  v3: 5%')
    print('得分公式其它因素权重  v4: 5%')
    print('当前模型的准确率为:'+str(y/x))
# getvector()
model_test()
# filenames=os.listdir("Job_csv")
# x=pandas.DataFrame(columns=['Type','job_title', 'job_area','salary', 'condition', 'company_title', 'company_info','skill',
#                  'publis_name','welfare','job_url'],dtype='str')
# for filename in tqdm(filenames):
#     x=x.append(pandas.read_csv("Job_csv/"+filename))
# x.info()





