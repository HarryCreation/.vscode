import scipy as sp
import numpy as np   #it is for creating a array to do fourier transformation
from scipy import fft   #we have to call fourier transformation form scipy 

Var1 = np.array(([2,4,6],[1,3,5]))
Hax = sp.fft.fft(Var1)
print(Hax)
