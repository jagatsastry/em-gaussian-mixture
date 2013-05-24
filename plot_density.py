from numpy import *
from matplotlib import *
import pylab
from pylab import *

mu = array([0.07238078, 2.59525552])
theta = array([ 0.51805198,  0.48194802])

def gaussian(x, idx=0, theta1=theta, mu1=mu):
    return theta1[idx]*exp(-1 * square(x - mu1[idx])/2)/sqrt(2*pi)
    
def gaussian1(x):
    return gaussian(x, 0)
    
def gaussian2(x):
    return gaussian(x, 1)
    
def mixture(x, theta1=theta, mu1=mu):
    return gaussian(x, 0, theta1, mu1) + gaussian(x, 1, theta1, mu1)

def plotDensity():
    x = numpy.linspace(-5,6,100) 

    y1 =  numpy.vectorize(gaussian1)(x)
    pylab.plot(x,y1, ".", label="Dist 1") 

    y3 = numpy.vectorize(gaussian2)(x)
    pylab.plot(x,y3, ".", label="Dist 2") 

    y2 = numpy.vectorize(mixture)(x)
    pylab.plot(x,y2, label="Gaussian mixture", linewidth=4) 

    pylab.xlabel("X")
    pylab.ylabel("p(x)")

if __name__ == "__main__":
    plotDensity()
    pylab.legend()
    pylab.show() # show the plot
