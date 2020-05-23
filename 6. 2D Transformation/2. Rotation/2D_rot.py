import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def rotateLine (x1, y1, x2, y2, theta):
  theta = math. radians (theta)
  plt.plot([x1, x2], [y1, y2])
  plt.plot([x1*math.cos(theta) - y1*math.sin(theta), x2*math.cos(theta) - y2*math.sin(theta)], [x1*math.sin(theta) + y1*math.cos(theta), x2*math.sin(theta) + y2*math.cos(theta) ])

rotateLine(0, 0, 100, 200, -45)
plt.show( )