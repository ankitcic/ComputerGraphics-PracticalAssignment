import matplotlib.pyplot as plt
import matplotlib.patches as patches

def scaleLine(x1, y1, x2, y2, s1, s2):
  plt.plot([x1, x2], [y1, y2])
  plt.plot([x1*s1, x2*s1], [y1*s2, y2*s2])

scaleLine(0, 0, 100, 200, 4, 3)
scaleLine(100, 200, 200, 0, 4, 3)
scaleLine(200, 0, 0, 0, 4, 3)
plt.show()