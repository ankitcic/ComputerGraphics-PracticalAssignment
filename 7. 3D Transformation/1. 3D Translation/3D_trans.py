import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = plt.axes(projection='3d')

def translateLine(x1, y1, z1, x2, y2, z2, t1, t2, t3):
  ax.plot([x1, x2], [y1, y2], [z1, z2])
  ax.plot([x1+t1, x2+t1], [y1+t2, y2+t2], [z1+t3, z2+t3])

translateLine(0, 0, 100, 200, 88, 1000, 45, 74, 36)
plt.show()