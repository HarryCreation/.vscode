import numpy
import matplotlib.pyplot as plt
from matplotlib import style

style.use("bmh")

x =[1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y=[100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]


Hax = numpy.poly1d(numpy.polyfit(x,y,3))
Hax1 = numpy.linspace(1,22,100)

plot = plt.figure()
plt.scatter(x,y)
plt.plot(Hax1,Hax(Hax1))
plt.xlabel("Hours")
plt.ylabel("Speed")
plt.show()