import pandas as pd
import seaborn as sp
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

Person = {'Finance':[1,3,6,8,3,4,6,2,3,4],
'Management':[2,5,6,7,8,3,4,2,3,8],
'Logistic':[2,4,2,5,6,3,4,3,5,6],
'get_work':[2,5,3,5,7,3,1,2,3,8]}

Data=pd.DataFrame(Person,columns=['Finance','Management','Logistic','get_work'])   

#Her we are separating the input and output data.
x = Data[['Finance', 'Management', 'Logistic']]
y = Data['get_work']

# Here we are separating the test data and training data for each other.
# the train_size function is for how many % data you want for test data.
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.3,random_state=0)

#Here we are calling for Logistic Regression model and save it in a Variable.
Logistic=LogisticRegression()

#Now we are fitting the data in a logistic regression model.
Logistic.fit(x_train,y_train)

# Here we are predicting the x_test data.
y_prediction = Logistic.predict(x_test)

# now we have to create a confusion metrices .
c_metrice = pd.crosstab(y_test,y_prediction,rownames=['Test y'], colnames=['pred y'])
sp.heatmap(c_metrice,annot=True)

print('Accuracy:',metrics.accuracy_score(y_test,y_prediction))
plt.show()