#Expectation Maximization of mixture of gaussians
#Author: Jagat Sastry P. 
#Starts with certain mu and theta
#Converges on mu=[ 0.07238078,  2.59525552], theta=[ 0.51805198,  0.48194802]

from numpy import *

def em(mu=array([1.0, 2.0]), theta=array([0.33, 0.67]), X=mat(genfromtxt("hw5.data.txt")).T, delta=0.001):
    n,m = shape(X)
    ylen = len(mu)
    p = mat(zeros((n, ylen)))
    diff = 1
    while diff > delta:
#E-STEP
        g = mat(zeros((n, ylen)))
        for i in range(n):
            g[i, :] = exp(-1 * square((X[i, :] - mu))/2)
        for y in range(ylen):
            p[:, y] = divide(theta[y]*g[:, y], theta[0] * g[:, 0] + theta[1] * g[:, 1])
#M-STEP
        prevMu = copy(mu)
        prevTheta = copy(theta)
        for y in range(ylen):
            theta[y] = sum(p[:, y])/n
            mu[y] = sum(multiply(X, p[:, y]))/sum(p[:, y])
        diff = sum(abs(mat(prevMu)-mat(mu)) + abs(mat(prevTheta) - mat(theta)))
        print mu, theta, prevMu, prevTheta

    return mu, theta


if __name__ == "__main__":
    print em()
