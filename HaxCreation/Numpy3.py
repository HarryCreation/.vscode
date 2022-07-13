import numpy as np

Var1 = np.array([(2,4,6),(1,3,5)])
Var2 = np.array([(2,3,9),(1,4,5)])

print(Var1.sum(axis=0))
print(Var1.sum(axis=1))
print(np.sqrt(Var1))
print(np.std(Var1))
print(np.exp(Var1))
print(np.log(Var1))
