import numpy as np
import matplotlib.pyplot as plt

def drawCircle(xc, yc, x, y):
    plt.scatter(xc + x, yc + y)
    plt.scatter(xc - x, yc + y)
    plt.scatter(xc + x, yc - y)
    plt.scatter(xc - x, yc - y)
    plt.scatter(xc + y, yc + x)
    plt.scatter(xc - y, yc + x)
    plt.scatter(xc + y, yc - x)
    plt.scatter(xc - y, yc - x)

def circleMid(xc, yc, r):
    x = r
    y = 0
    plt.scatter(x, y)
    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
           P = P + 2 * y + 1
        else:
            x -= 1
            P = P+2* y-2* x +1
        if (x < y):
            break
        drawCircle(xc, yc, x, y)

circleMid(5, 10, 15)
plt.show()