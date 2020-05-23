import numpy as np
import matplotlib.pyplot as plt

def drawDDA(x1,y1,x2,y2):
  x,y = x1,y1
  length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
  dx = (x2 - x1) / float(length)
  dy = (y2 - y1) / float(length)
  print('x = %s, y = %s' % (((x, y))))
  plt.scatter(x, y)
  for i in range(length):
    x += dx
    y += dy
    print('x = %s, y = %s' % (((x, y))))
    plt.scatter(x, y)


drawDDA(2, 5, 8,15)
plt.show( )