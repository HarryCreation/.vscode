import numpy as np

Var1 = np.array([2,4,6])
Var2 = np.array([(2,4,6),(1,3,5)])
Var1 = Var1.reshape(1,3)
Var2 = Var2.reshape(3,2)
print(Var1.itemsize)
print(Var2.itemsize)
print(Var1.dtype)
print(Var2.dtype)
print(Var1.ndim)
print(Var2.ndim)
print(Var1.shape)
print(Var2.shape)
