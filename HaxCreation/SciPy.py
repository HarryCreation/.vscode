import scipy as integrate
from scipy import integrate
f = lambda x, y : x*y**2
i = integrate.dblquad(f, 0, 1, lambda x:0, lambda x:1)
print(i)






