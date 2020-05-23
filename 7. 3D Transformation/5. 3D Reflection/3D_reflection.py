import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = plt.axes(projection='3d')

def reflectLine(x1, y1, z1, x2, y2, z2):
  plt.plot([x1, x2], [y1, y2], [z1, z2])
  plt.plot([x1, x2], [y1, y2], [-z1, -z2])

print("Reflection around XY axis: ")
reflectLine(0, 84, 100, 200, 475, 368)
reflectLine(200, 475, 368, 524, 712, 100)
reflectLine(524, 712, 100, 0, 84, 100)
plt.show( )