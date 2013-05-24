import numpy as np
import pylab as pl
from sklearn import mixture
from plot_density import *

def get_ll(X, mu):
    sm = 0
    for x in X:
        sm += log(mixture(x, [0.5, 0.5], mu))
    return sm

mu1 = arange(-1, 4, 0.25)
mu2 = arange(-1, 4, 0.25)

data = genfromtxt("hw5.data.txt")

Z = [[get_ll(data, [mu1x, mu2y]) for mu1x in mu1] for mu2y in mu2]
print Z
print shape(Z)
X = mu1
Y = mu2
pl.title("Contour plot of log likelihood vs the two means of the mixture model")
pl.xlabel("mu1")
pl.ylabel("mu2")
CS = pl.contour(X, Y, Z)
CB = pl.colorbar(CS, shrink=0.8, extend='both')

pl.axis('tight')
pl.show()
