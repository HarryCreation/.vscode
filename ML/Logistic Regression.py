from pyexpat import model
import pandas as pd
import seaborn as sp
import matplotlib.pyplot as plt
from sklearn.linear_model import model
from sklearn.linear_model import LogisticRegression

Var1 = pd.read_csv("C:\\Users\\hvwag\\OneDrive\Desktop\\HaxCreation.csv")
x = Var1[['Age']]
y = Var1[['Bought_Insurance']]
plt.scatter(x,y)

model.logisticregression()
model.fit(x,y)

Hax = model.predict(x)
Var1['Hax'] = Hax
Var1
sp.regplot(x,y,Var1,logistic=True)