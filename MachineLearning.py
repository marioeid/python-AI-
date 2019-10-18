from __future__ import print_function
 
import  math
 
def class_count(dataset):
    counts={}
  #  print("data set :",dataset)
    for row in dataset:
 
      #  print(row)
        l=row[-1]
 
       # print(type(l))
        if l not in counts.keys():
            counts[l]=0
        counts[l]+=1
 
 
    return  counts
class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense
 
class Question:
    def __init__(self,index,val):
        self.index=index
        self.val=val
 
    def ans(self,feature):
        val=feature[self.index]
        return  val==self.val
 
class descision_node:
    def __init__(self,question,true,false):
        self.question=question
        self.true=true
        self.false=false
 
class leaf:
    def __init__(self,dataset):
        self.prediction=class_count(dataset)
 
 
 
 
class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1
 
class ID3:
    def __init__(self, features):
        self.features = features
 
 
    def classify(self, row,node):
            if isinstance(node, leaf):
                for i in node.prediction:
                    return  i
 
            if node.question.ans(row):
                return self.classify(row, node.true)
            else:
                return self.classify(row, node.false)
 
 
def entropycalc(data):
    counts=class_count(data)
    entropy=0.0
    for instance in counts:
        prob_of_inst=counts[instance]/float(len(data))
        entropy-=prob_of_inst*math.log(prob_of_inst,2)
    return  entropy
 
def info_gain(left,right,current_impurity):
    p=float(len(left))/(len(left)+len(right))
    return  current_impurity - p*entropycalc(left) -(1-p)*entropycalc(right)
 
 
def partition(data,question):
    true_rows,false_rows=[],[]
    for row in data:
 
        if question.ans(row):
            true_rows.append(row)
        else :
            false_rows.append(row)
 
    return  true_rows,false_rows
def best_quesiton_to_ask(data):
    best_gain=0
    best_question=None
    current_impuirty=entropycalc(data)
    n_features=len(data[0])-1
    for col in range(n_features):
 
      values=set(row[col] for row in data)
      for val in values:
          question=Question(col,val)
          true_rows,false_rows=partition(data,question)
          if len(true_rows)==0 or len(false_rows)==0:
              continue
          gain=info_gain(true_rows,false_rows,current_impuirty)
          if gain>best_gain:
              best_gain,best_question=gain,question
 
    F=Feature
    if (col==0):
         F=Feature('age')
    elif (col==1):
         F=Feature('prescription')
    elif (col==2):
         F=Feature('astigmatic')
    elif (col==3):
         F=Feature('astigmatic')
    elif (col==4):
         F=Feature('tearRate')
 
    F.infoGain=best_gain
    return  best_gain,best_question
def build_Tree(dataset):
 
    gain,question=best_quesiton_to_ask(dataset)
 
    if gain==0:
        return leaf(dataset)
 
    true_rows,false_rows=partition(dataset,question)
    true_branch=build_Tree(true_rows)
    false_branch=build_Tree(false_rows)
 
    return  descision_node(question,true_branch,false_branch)
 
 
def print_leaf(counts):
    total=sum(counts.values())*1.0
    probs={}
    for val in counts.keys():
        probs[val]=str(int(counts[val]/total*100))+"%"
    return  probs
 
 
 
 
def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0,	labels[0]))
    data.append(item(0, 0, 0, 1,	labels[1]))
    data.append(item(0, 0, 1, 0,	labels[2]))
    data.append(item(0, 0, 1, 1,	labels[3]))
    data.append(item(0, 1, 0, 0,	labels[4]))
    data.append(item(0, 1, 0, 1,	labels[5]))
    data.append(item(0, 1, 1, 0,	labels[6]))
    data.append(item(0, 1, 1, 1,	labels[7]))
    data.append(item(1, 0, 0, 0,	labels[8]))
    data.append(item(1, 0, 0, 1,	labels[9]))
    data.append(item(1, 0, 1, 0,	labels[10]))
    data.append(item(1, 0, 1, 1,	labels[11]))
    data.append(item(1, 1, 0, 0,	labels[12]))
    data.append(item(1, 1, 0, 1,	labels[13]))
    data.append(item(1, 1, 1, 0,	labels[14]))
    data.append(item(1, 1, 1, 1,	labels[15]))
    data.append(item(1, 0, 0, 0,	labels[16]))
    data.append(item(1, 0, 0, 1,	labels[17]))
    data.append(item(1, 0, 1, 0,	labels[18]))
    data.append(item(1, 0, 1, 1,	labels[19]))
    data.append(item(1, 1, 0, 0,	labels[20]))
    return data
 
 
 
dataset = getDataset()
newdataset=[]
for instance in dataset:
    row=[]
    row.append(instance.age)
    row.append(instance.prescription)
    row.append(instance.astigmatic)
    row.append(instance.tearRate)
    row.append(instance.needLense)
    newdataset.append(row)
features = [Feature('age'),Feature('prescription'),Feature('astigmatic'),Feature('tearRate')]
 
 
 
best_quesiton_to_ask(newdataset)
tree=build_Tree(newdataset)
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1],tree) # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0],tree) # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0],tree) # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1],tree) # should print 1
print('testcase 4: ', cls)