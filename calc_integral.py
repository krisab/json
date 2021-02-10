import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def f(x):
    #return x*x + x + 1
    #return math.sin(x)
    #return math.tan(x)
    return math.log(x + x*x)

def calcInterval(a, step):
    return 0.5 * f(a) + f(a+step) * step

def calcIntegral (a, n, step):
    integral = 0
    for i in range(n):
        integral = calcInterval(a, step)
        a = a + step
    return integral

def main():
    a = 1
    #b = 1
    #b=math.pi/2
    b=4
    n = 50
    step = (b-a) / n
    Inter = calcIntegral(a, n, step)
    Err = 11/6 - Inter
    print(11/6, '\t', Inter, '\t', Err)

    #xs = [i for i in np.arange(a,b+step,step)]
    xs = list(np.arange(a,b+step,step))
    ys = [f(i) for i in np.arange(a,b+step, step)]
    #print (ys)

    plt.plot(xs, ys)
    #plt.plot(xs, ys, 'ro')
    #plt.plot(xs,ys, 'r-o')
    plt.fill_between(xs, ys, facecolor='yellow', alpha=0.5)
    plt.show()

if __name__ == '__main__': main()