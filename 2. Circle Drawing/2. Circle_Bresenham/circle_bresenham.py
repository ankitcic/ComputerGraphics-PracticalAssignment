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

def circleBres(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    drawCircle(xc, yc, x, y)
    while (y >= x):
        x += 1
        if (d > 0):
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
             d=d+4* x + 6
        drawCircle(xc, yc, x, y)

circleBres(15, 60, 30)
plt.show()