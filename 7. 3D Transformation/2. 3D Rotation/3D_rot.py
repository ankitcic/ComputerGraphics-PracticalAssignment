import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

fig = plt.figure()
ax = plt.axes(projection='3d')

def rotateLine (x1, y1, z1, x2, y2, z2, theta):
  theta = math. radians (theta)
  ax.plot([x1, x2], [y1, y2], [z1, z2])
  plt.plot([x1*math.cos(theta) - y1*math.sin(theta), x2*math.cos(theta)- y2*math.sin(theta)], [x1*math.sin(theta) + y1*math.cos(theta),x2*math.sin(theta) + y2*math.cos(theta)], [z1, z2])

print("Rotation around Z-axis: ")
rotateLine(0, 0, 110, 220, 90, 1200, 380)
plt.show( )