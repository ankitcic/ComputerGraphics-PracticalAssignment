import numpy as np
import matplotlib.pyplot as plt


def bresenham(x1, y1, x2, y2):

    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2+1):
        plt.scatter(x, y)
        print(" (", x, " , ", y, ") \n")

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
    if (slope_error_new >= 0):
        y = y+1
        slope_error_new = slope_error_new - 2 * (x2 - x1)


if __name__ == '__main__':
    x1 = 5
    y1 = 5
    x2 = 12
    y2 = 12
    bresenham(x1,y1 , x2, y2)
    plt.show()