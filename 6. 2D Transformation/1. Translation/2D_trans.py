import matplotlib.pyplot as plt
import matplotlib.patches as patches


def translateline(x1, y1, x2, y2, t1, t2):
    plt.plot([x1, x2], [y1, y2])
    plt.plot([x1 + t1, x2 + t1], [y1 + t2, y2 + t2])


translateline(5, 8, 12, 15, 5, 6)
plt.show()
