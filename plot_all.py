from numpy import *
from pylab import *
from plot_density import *

X = genfromtxt("hw5.data.txt")
xlim((-5, 6))
hist(X, bins=30, label="Histogram of hw5.data", normed=True)
axvline(x=0.07238078, color="k", linestyle='dashed', linewidth='4', label='Mean1=0.072')
axvline(x=2.59525552,  color="k", linestyle='dashed', linewidth='4', label='Mean2=2.595')

plotDensity()
legend()
show()
