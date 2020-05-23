import matplotlib.pyplot as plt
def midptellipse(rx, ry, xc, yc):
    x = 0
    y = ry
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while (dx < dy):
        plt.scatter(xc + x, yc+y)
        plt.scatter(xc - x, yc+y)
        plt.scatter(xc + x, yc - y)
        plt.scatter(xc - x, yc - y)

        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))
    while (y >= 0):
        plt.scatter(xc + x, yc + y)
        plt.scatter(xc - x, yc + y)
        plt.scatter(xc + x, yc - y)
        plt.scatter(xc - x, yc - y)

        if (d2 > 0):
          y -= 1
          dy = dy - (2 * rx * rx)
          d2 = d2 + (rx * rx) - dy
        else:
           y -= 1
           x += 1
           dx = dx + (2 * ry * ry)
           dy = dy - (2 * rx * rx)
           d2 = d2 + dx - dy + (rx * rx)

midptellipse(20, 40, 60, 90)
plt.show()
