import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


#first upload data
Data = pd.read_csv("E:\\One Drive Pro\\OneDrive - Microsoft 365\\Internet_Data.csv")

#Data visualise 
Data.plot(kind="scatter",x="INTERNET/Mbps",y="DATA/DAY")
plt.show()

#correlation coefficients
Data.corr()

#changing the dataframe of the varaiable
Internet_use = pd.DataFrame(Data["INTERNET/Mbps"])
DATA_use = pd.DataFrame(Data["DATA/DAY"])


#Builing Linear Regression Model
LR = linear_model.LinearRegression()
Model=LR.fit(Internet_use,DATA_use)

H = Model.coef_
print(H)