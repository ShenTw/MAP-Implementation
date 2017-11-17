# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:23:14 2017

@author: shen
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:14:36 2017

@author: shen
"""

submissionList = []
submissionDic = {}
solutionDic = {}
APList = []
APSum = 0
MAP=0
path = 'C:/Users/shen/.spyder-py3/'
with open(path+'solution.txt','r') as A:
    line = A.readline() 
    #棄置第一行
    
    for line in A.readlines():
        temp = [] 
        line = line.strip('\n')
        temp = line.split(',')
        queryName = temp[0]
        solutions = temp[1].split()
        solutionDic[queryName] = solutions
        
""" test solutionDic
    for q in solutionDic:
        print(q,": ",solutionDic[q])
"""  

with open (path+'HW1_M10615103.txt','r') as S:
    line = S.readline()
    for line in S.readlines():
        temp = []
        line = line.strip('\n')
        temp = line.split(',')
        queryName = temp[0]
        submissions = temp[1].split()        
        submissionDic[queryName] = submissions
""" test submissionDic
    for q in submissionDic:
        print(q,": ",submissionDic[q])
"""


"""
開始計算MAP步驟
1. need submissionDic , solutionDic ,即可
"""
for key in submissionDic:                 #特定query
    PSum = 0                             #每個query要重新計算的
    countAll = 0
    countR = 0
    PList = []
    for d in submissionDic[key]:          #特定query下之特定doc排序
        countAll = countAll+1             #每拿出一個文件分母+1
        for dA in solutionDic[key]:       #特定query下之所有相關文件
            if dA==d :
                countR = countR+1
                PList.append(countR/countAll)
                #print("got it ! : solution: " ,dA," sub: ",d)
    for P in PList:                  #一個query一組APlist,一個APsum
        PSum = PSum + P
    
    APList.append(PSum/len(PList)) #把AP算出來
    
for AP in APList:
    APSum = APSum+AP
 
MAP = APSum/len(solutionDic)
print("MAP score is : ",MAP)
