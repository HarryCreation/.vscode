import numpy as np

Var = np.linspace(1,50,10)
Var1 = np.array([(2,4,6),(1,3,5)])
Var2 = np.array([2,3,8])
Var3 = np.array([(2,4,6),(1,3,5),(7,3,4)])
print(Var1[0,2])
print(Var3[0,1])
print(Var1.max())
print(Var2.min())
print(Var3.sum())



