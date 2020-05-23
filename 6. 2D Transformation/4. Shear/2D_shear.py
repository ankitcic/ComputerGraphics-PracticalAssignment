import matplotlib.pyplot as plt
import matplotlib.patches as patches

def shearLine(x1, y1, x2, y2, sh1, sh2):
  plt.plot([x1, x2], [y1, y2])
  plt.plot([x1+sh1*y1, x2+sh1*y2], [y1, y2])
  plt.plot([x1, x2], [y1+sh2*x1, y2+sh2*x2])

print("The new coordinates after shearing in X and Y direction (independently) are:")

shearLine(10, 12, 18, 30, 2, 3)
shearLine(18, 30, 30, 10, 2, 3)
shearLine(30, 10, 10, 12, 2, 3)
plt.show()