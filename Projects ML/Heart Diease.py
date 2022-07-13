import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

Heart_data = pd.read_csv('C:\\Users\\hvwag\\OneDrive\\Desktop\\heart.csv.xls')

s = Heart_data['target'].value_counts()

#splitting the data into features and labels.
x = Heart_data.drop(columns='target',axis= 1)
y = Heart_data['target']

#spliiting the data into training data & test data.
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)

#model training logistic regression
model = LogisticRegression()

#fitting the data into model
model_fit=model.fit(x_train,y_train)

# model evaluation,accuracy rate on training data.
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction,y_train)

# accuracy rate of test data.
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction,y_test)

#now buliding the predective sysytem.
input_data = (57,1,0,140,192,0,1,148,0,0.4,1,0,1)

# changing the tuple data into array.
input_data_array = np.asarray(input_data)

# reshaping the array as we are predecting for only on one data point.
input_data_reshaped =input_data_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)

print(prediction)