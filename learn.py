import operator
dataset=[
        [1,1,'y'],
        [1,0,'y'],
        [0,1,'n'],
        [0,0,'n'],
        [0, 0, 'n']
    ]

numFeaturea =len(dataset[0])-1



def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        else: classCount[vote]+=1
    #对字典按值排序（降序），获取次数最大类别
    sortedClasscount=sorted(classCount.items(),key=lambda x:x[1], reverse=True)
    return sortedClasscount[0][0]


classList=[exam[-1] for exam in dataset]
print(classList)
print(majorityCnt(classList))
