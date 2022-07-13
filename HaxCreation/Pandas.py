import pandas as pd 

Employee_new ={'Name':['A','B','C'],'Salary':[10,20,2],'Bonus in %':[5,4,4,]}
Employee_old ={'Name':['A','B','C'],'Salary':[10,2,30],'Bonus in %':[5,0,4,]}


T1=pd.DataFrame(Employee_new)
T2=pd.DataFrame(Employee_old)

Company = pd.merge(T1,T2,on='Salary')
print(Company)




