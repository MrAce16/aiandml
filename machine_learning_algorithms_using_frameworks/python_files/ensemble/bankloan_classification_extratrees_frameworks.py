
# KNN Classification
from pandas import read_csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
filename = '../../datasets/bankloan_classification_train.csv'
names = ['age', 'loanamount', 'status']
df = read_csv(filename, names=names)
array = df.values
inputx = array[:,0:2]
outputy = array[:,2]
thismodel = ExtraTreesClassifier(n_estimators=100)
print(thismodel.fit(inputx,outputy))
filename = '../../datasets/bankloan_classification_test.csv'
names = ['age', 'loanamount']
newdataframe = read_csv(filename, names=names)
array = newdataframe.values
testinputz = array[0:4,0:2]
print(newdataframe)
res=thismodel.predict(testinputz)
reslist=[]
for val in res:
    if val==0:
        reslist.append("WillNotPay")
    else:
        reslist.append("WillPay")
print(reslist)
res=thismodel.predict(testinputz)
print(thismodel.predict(testinputz))
