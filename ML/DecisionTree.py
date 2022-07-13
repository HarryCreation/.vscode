import sklearn
from sklearn import tree
features = [[2,100],[6,25],[1,300],[1,1000],[4,100],[10,100]]
Label = [1,2,1,1,2,2]
Var1= tree.DecisionTreeClassifier()
Var2 = Var1.fit(features,Label)
print(Var2.predict([[1,150]]))
