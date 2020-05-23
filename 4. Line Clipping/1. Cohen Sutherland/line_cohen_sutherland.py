import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS
from matplotlib import pyplot as plt

# Code Start here
im = Image.new("RGB", (640, 480))
im1 = Image.new("RGB", (640, 480))
draw = ID.Draw(im)
draw2 = ID.Draw(im1)
draw.polygon((200, 200, 400, 200, 400, 300, 200, 300), outline=255)
draw2.polygon((200, 200, 400, 200, 400, 300, 200, 300), outline=255)
p1 = (
400.0, 300.0)  # point p1 and p4 are perfect for drawing a rectangle but for simplicity sake p2 and p3 are considered
p4 = (200.0, 200.0)


def computeCode(x, y):
    #     print("\n(%d,%d) and (%d,%d)\n"%(p1[0],p1[1],p4[0],p4[1]))
    code = 0
    if x < p4[0]:
        code = code | 1
    elif x > p1[0]:
        code = code | 2
    if y < p4[1]:
        code = code | 4
    elif y > p1[1]:
        code = code | 8
    return code


def cohenSutherlandClip(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    while True:
        #         print("(%d,%d) and (%d,%d) %d %d" % (x1,y1,x2,y2,code1,code2));
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break;
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            if code_out & 8:
                x = x1 + (x2 - x1) * (p1[1] - y1) / (y2 - y1)
                y = p1[1]
            elif code_out & 4:
                x = x1 + (x2 - x1) * (p4[1] - y1) / (y2 - y1)
                y = p4[1]
            elif code_out & 2:
                y = y1 + (y2 - y1) * (p1[0] - x1) / (x2 - x1)
                x = p1[0]
            elif code_out & 1:
                y = y1 + (y2 - y1) * (p4[0] - x1) / (x2 - x1)
                x = p4[0]
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        ## Commenting print line due to unnnecessary output. Can be uncommonted if any testing is performed
        #         print ("Accepted Straigth Line from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2))
        draw2.line((x1, y1, x2, y2), fill=(0, 0, 255))

    else:
        print("This line can not be drawn as outside the area")


def clip(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(0, 255, 0))
    cohenSutherlandClip(x1, y1, x2, y2)


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

clip(x1, y1, x2, y2)
im.show()
im1.show()
