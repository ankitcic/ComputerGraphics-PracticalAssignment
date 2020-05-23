import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = plt.axes(projection='3d')

def shearLine(x1, y1, z1, x2, y2, z2, sh1, sh2, sh3):
    plt.plot([x1, x2], [y1, y2], [z1, z2])
    plt.plot([x1 + sh1 * y1, x2 + sh1 * y2], [y1, y2], [z1 + sh3 * y1, z2 + sh3 * y2])
    plt.plot([x1, x2], [y1 + sh2 * x1, y2 + sh2 * x2], [z1 + sh3 * x1, z2 + sh3 * x2])
    plt.plot([x1 + sh1 * z1, x2 + sh1 * z2], [y1 + sh2 * z1, y2 + sh2 * z2], [z1, z2])

print("The new coordinates after shearing in x, y and z direction (independently) are:")

shearLine(0, 84, 100, 200, 475, 368, 2, 3, 4)
shearLine(200, 475, 368, 524, 712, 100, 2, 3, 4)
shearLine(524, 712, 100, 0, 84, 100, 2, 3, 4)
plt.show()