import numpy as np
import matplotlib.pyplot as plt

x = np.array([23,34,45,67,54,65,36,39,65,34,40,56,69])
y = np.array([73,54,35,36,76,53,21,32,34,57,72,45,55])

Var1 = np.polyfit(x,y,1)

plt.plot(x,y,'*')
plt.plot(x,np.polyval(Var1,x),'r-')
plt.show()
