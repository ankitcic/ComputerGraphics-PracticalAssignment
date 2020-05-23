import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = plt.axes(projection='3d')

def scaleLine(x1, y1, z1, x2, y2, z2, s1, s2, s3):
  plt.plot([x1, x2], [y1, y2], [z1, z2])
  plt.plot([x1*s1, x2*s1], [y1*s2, y2*s2], [z1*s3, z2*s3])

scaleLine(0, 84, 100, 200, 475, 368, 4, 3, 2)
scaleLine(200, 475, 368, 524, 712, 100, 4, 3, 2)
scaleLine(524, 712, 100, 0, 84, 100, 4, 3, 2)
plt.show()