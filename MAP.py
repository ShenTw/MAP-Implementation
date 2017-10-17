# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:14:36 2017

@author: shen
"""

submissionList = []
submissionDic = {}
solutionDic = {}
APList = []
APSumList = []
MAP = 0
with open('submission.txt','r') as S:
    for line in S.readlines():
        submissions  = line
        
        
"""

for key in submissionDic:                 #特定query
    APSum = 0                             #每個query要重新計算的
    countAll = 0
    countR = 0
    for d in submissionDic[key]:          #特定query下之特定doc
        for dA in solutionDic[key]:       #特定query下之所有解答
            if dA==d :
                countAll = countAll+1
                countR = countR+1
                APList.append(countR/countAll)
            else:
                countAll = countAll+1
                
    for AP in APList:
        APSum = APSum + AP
    
    APSumList.append(APSum)

for AP in APSumList:
    MAP = MAP+AP
    
MAP = MAP/len(solutionDic)

"""