from math import  log
import operator

#计算数据集合的无序程度：熵，信息增益为熵差
def CalShannonEnt(dataset):
    numEntries=len(dataset) #计算数据集实例个数
    labelCounts={}#赋值数据集最后一列
    shannonEnt = 0.0 #熵值

    # 若键值不存在，将键值加入字典，否则不记录，仅增加记录次数
    for featVec  in dataset:
        currentLabel=featVec[-1]

        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0

        labelCounts[currentLabel]+=1


    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        #print(prob)
        shannonEnt -= prob*log(prob,2)

    return shannonEnt


def createDataSet():
    dataset=[
        [1,1,'y'],
        [1,1,'n'],
        [0,1,'n'],
        [1,0,'n'],
        [0, 1, 'n']
    ]
    labels=['no surface' ,'filppers']
    return dataset ,labels

#按照给定特征划分数据集合，三个参数分别为 待处理数据集、划分数据集特征，需要返回特征的值
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    #对数据集中每一个子集，如果其划分列为指定值，返回划分列前的数据集
    for featvec in dataSet:
        if featvec[axis]==value:
            reducedFeatvec=featvec[:axis]#取划分列前的元素
            reducedFeatvec.extend(featvec[axis+1:])#增加特征值
            retDataSet.append(reducedFeatvec)
    return retDataSet


#获取最好的划分特征
def chooseBestFeature(dataSet):
    numFeaturea=len(dataSet[0])-1#计算分类值以外的元素数目
    baseEntroy=CalShannonEnt(dataSet)#信息熵

    bestInfoGain=0.0
    bestFeature=-1

    #对分类结果值以外的所有列计算其熵
    for i in range(numFeaturea):
        featList=[example[i] for example in dataSet]#取dataset所有子集第一个元素
        uniqueVal=set(featList)#从列表中创建集合，获取列表不重复元素的最快方法
        newEntropy=0.0

        for value in uniqueVal:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*CalShannonEnt(subDataSet)

        infogain=baseEntroy-newEntropy

        if (infogain > bestInfoGain):
            bestInfoGain=infogain
            bestFeature=i

    return bestFeature,bestInfoGain

#获取出现次数最多的类别：注 python3中iteritems()方法不再支持，对字典排序如下。
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        else: classCount[vote]+=1
    #对字典按值排序（降序），获取次数最大类别，按键排序设置lambda表达式为x[0]
    sortedClasscount=sorted(classCount.items(),key=lambda x:x[1], reverse=True)
    return sortedClasscount[0][0]



mydata,lab=createDataSet()

# mydata[0][-1]='maybe'

print(CalShannonEnt(mydata))
print(chooseBestFeature(mydata))
