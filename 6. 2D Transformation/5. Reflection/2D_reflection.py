import matplotlib.pyplot as plt
import matplotlib.patches as patches

def translateLine(x1, y1, x2, y2):
  plt.plot([x1, x2], [y1, y2])
  plt.plot([-x1, -x2], [y1, y2])

print("Reflection around X axis: ")
translateLine(42, 125, 100, 200)
plt.show()