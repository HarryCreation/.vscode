import scipy as sp

#it is for creating a array we have to import numpy to do linear algebra
import numpy as np

#we have call linear algebra subpackage to perform
from  scipy import linalg

Var1 = np.array(([1,3],[2,4]))
Var2 = np.array(([5,9],[6,8]))

Hax = sp.linalg.solve(Var1,Var2)
Hax1= sp.linalg.inv(Var1) # it is inverse of the array 
print(Hax)
print(Hax1)
