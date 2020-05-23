
import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS
import time
import numpy as np

## Code Starts here
im = Image.new("RGB", (500,500))
im1= Image.new("RGB", (500,500))
draw2=ID.Draw(im1)
draw = ID.Draw(im)
draw.polygon((162, 110, 388, 19, 386, 103, 162, 247), outline = 255)
draw2.polygon((162, 110, 388, 19, 386, 103, 162, 247), outline = 255)

draw.polygon((242, 78, 480, 77, 480, 289, 242, 289), outline = 'green')

S = "242 78 480 77 480 289 242 289"
C = "162 110 388 19 386 103 162 247"

def draw1(x1, y1, x2, y2):
    draw2.line((x1,y1,x2,y2),fill=(0,255,0))

class baseVertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vertex(baseVertex):
    def __init__(self, x, y, next = None):
        super(Vertex, self).__init__(x, y)
        self.next = next

class Intersection(baseVertex):
    def __init__(self, x, y, nextS = None, nextC = None, crossDi = -1):
        super(Intersection, self).__init__(x, y)
        self.nextS = nextS
        self.nextC = nextC
        self.crossDi = crossDi
        self.used = False

def floatEqual(f1, f2):
    prec = 1e-5
    if abs(f1 - f2) < prec:
        return True
    else:
        return False
def floatLarger(f1, f2):
    if floatEqual(f1, f2):
        return False
    elif f1 > f2:
        return True
    else:
        return False

def isVertexInPolygon(v, list):
    judgeIndex = 0
    for i in range(len(list)):
        j = i + 1
        minY = min(list[i % len(list)].y, list[j % len(list)].y)
        maxY = max(list[i % len(list)].y, list[j % len(list)].y)
        if floatLarger(v.y, maxY) or floatLarger(minY, v.y):
            continue
        if floatEqual(maxY, minY):
            if floatLarger(v.x, max(list[i % len(list)].x, list[j % len(list)].x)):
                judgeIndex += 1
                continue
            elif floatLarger(min(list[i % len(list)].x, list[j % len(list)].x), v.x):
                continue
            else:
                return True
        x = (list[i % len(list)].x - list[j % len(list)].x) / (list[i % len(list)].y - list[j % len(list)].y) * (v.y - list[i % len(list)].y) + list[i % len(list)].x
        if(floatEqual(v.x, x)):
            return None
        if floatLarger(v.x, x):
            judgeIndex += 1
    if judgeIndex % 2 != 0:
        return True
    return False

def getX(v):
    return v.x
def getY(v):
    return v.y

def LineCrossH(y, c1, c2):
    return c1.x + (c2.x - c1.x) * (y - c1.y) / (c2.y - c1.y)
def LineCrossV(x, c1, c2):
    return c1.y + (c2.y - c1.y) * (x - c1.x) / (c2.x - c1.x)

def CutByVerticalLine(s1, s2, list):
    assert floatEqual(s1.x, s2.x)
    crossXs = []
    x = s1.x

    shearedList = [Vertex(r.x, r.y) for r in list]

    minY = min(s1.y, s2.y)
    maxY = max(s1.y, s2.y)

    for i in range(len(list)):
        vertex = list[i]
        c1 = shearedList[i % len(list)]
        c2 = shearedList[(i + 1) % len(list)]

        if(floatEqual(c1.x, c2.x) and floatEqual(c1.x, x)):
            continue
        if(floatLarger(c1.x, x) and floatLarger(c2.x, x)):
            continue
        if(floatLarger(x, c1.x) and floatLarger(x, c2.x)):
            continue

        y = float('%.9f' % LineCrossV(x, c1, c2))

        inters = Intersection(x, y)

        next = None
        if((floatLarger(y, minY) and floatLarger(maxY, y))
         or (c2.y == y and x == s2.x)
         or (c1.y == y and x == s1.x)
            or (floatEqual(c2.x, x) and floatEqual(y, s1.y))
            or (floatEqual(c1.x, x) and floatEqual(y, s2.y))
            or (floatEqual(y, minY) and (not floatEqual(c1.x, x)) and (not floatEqual(c2.x, x)))
            or (floatEqual(y, maxY) and (not floatEqual(c1.x, x)) and (not floatEqual(c2.x, x)))):
            while not ((isinstance(vertex, Vertex) and isinstance(vertex.next, Vertex)) or (isinstance(vertex, Intersection) and isinstance(vertex.nextS, Vertex))):
                if isinstance(vertex, Vertex):
                    assert isinstance(vertex.next, Intersection)
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.next.x, inters.x)) or (floatLarger(c1.x, c2.x) and floatLarger(inters.x, vertex.next.x)):
                        break
                    vertex = vertex.next
                else:
                    assert isinstance(vertex.nextS, Intersection)
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.nextS.x, inters.x)) or (floatLarger(c1.x, c2.x) and floatLarger(inters.x, vertex.nextS.x)):
                        break
                    vertex = vertex.nextS
            if isinstance(vertex, Vertex):
                next = vertex.next
            else:
                next = vertex.nextS
            if isinstance(vertex, Vertex):
                vertex.next = inters
            else:
                assert isinstance(vertex, Intersection)
                vertex.nextS = inters
            inters.nextS = next
            if floatEqual(c1.x, x):
                assert not floatEqual(c2.x, x)
                if floatLarger(c2.x, x):
                    inters.crossDi = 0
                else:
                    inters.crossDi = 1
            elif floatLarger(c1.x, x):
                inters.crossDi = 1
            else:
                inters.crossDi = 0
            if floatLarger(s2.y, s1.y):
                inters.crossDi = 0 if inters.crossDi == 1 else 1

            print("s1:%s, s2:%s, c1:%s, c2:%s, inter:%s, crossDi:%s" % (("%f, %f" % (s1.x, s1.y)), ("%f, %f" % (s2.x, s2.y)), ("%f, %f" % (c1.x, c1.y)), ("%f, %f" % (c2.x, c2.y)), ("%f, %f" % (inters.x, inters.y)), ("%s" % ("in" if inters.crossDi == 0 else "out"))))
            crossXs.append(inters)
    return crossXs
def CutByLine(s1, s2, list):
    print("s1 = %s, s2 = %s" % (("%f, %f" % (s1.x, s1.y)), ("%f, %f" % (s2.x, s2.y))))

    if floatEqual(s1.x, s2.x):
        return CutByVerticalLine(s1, s2, list)
    crossXs = []

    slope = (s2.y - s1.y) / (s1.x - s2.x)
    y = s1.x * slope + s1.y
    shearedList = [Vertex(r.x, r.x * slope + r.y) for r in list]

    minX = min(s1.x, s2.x)
    maxX = max(s1.x, s2.x)

    for i in range(len(list)):
        vertex = list[i]
        c1 = shearedList[i % len(list)]
        c2 = shearedList[(i + 1) % len(list)]
        print("c1 = %s, c2 = %s" % (("%f, %f" % (c1.x, c1.y - c1.x * slope)), ("%f, %f" % (c2.x, c2.y - c2.x * slope))))

        if(floatEqual(c1.y, c2.y) and floatEqual(c1.y, y)):
            continue
        if(floatLarger(c1.y, y) and floatLarger(c2.y, y)):
            continue
        if(floatLarger(y, c1.y) and floatLarger(y, c2.y)):
            continue

        x = float('%.9f' % LineCrossH(y, c1, c2))
        npy = y - x * slope
        inters = Intersection(x, npy)

        next = None
        if((floatLarger(x, minX) and floatLarger(maxX, x))
        or (c2.y == y and x == s2.x)
        or (c1.y == y and x == s1.x)
        or (floatEqual(c2.y, y) and floatEqual(x, s1.x))
        or (floatEqual(c1.y, y) and floatEqual(x, s2.x))
        or (floatEqual(x, minX) and (not floatEqual(c1.y, y)) and (not floatEqual(c2.y, y)))
        or (floatEqual(x, maxX) and (not floatEqual(c1.y, y)) and (not floatEqual(c2.y, y)))):
            while not ((isinstance(vertex, Vertex) and isinstance(vertex.next, Vertex)) or (isinstance(vertex, Intersection) and isinstance(vertex.nextS, Vertex))):
                if isinstance(vertex, Vertex):
                    assert isinstance(vertex.next, Intersection)
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.next.x, inters.x)) \
                            or (floatLarger(c1.x, c2.x) and floatLarger(inters.x, vertex.next.x))\
                            or (floatLarger(c1.y - c1.x * slope, c2.y - c2.x * slope) and floatLarger(inters.y, vertex.next.y))\
                            or (floatLarger(c2.y - c2.x * slope, c1.y - c1.x * slope)  and floatLarger(vertex.next.y, inters.y)):
                        break
                    vertex = vertex.next
                else:
                    assert isinstance(vertex.nextS, Intersection)
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.nextS.x, inters.x))\
                            or (floatLarger(c1.x, c2.x) and floatLarger(inters.x, vertex.nextS.x))\
                            or (floatLarger(c2.y - c2.x * slope, c1.y - c1.x * slope) and floatLarger(inters.y, vertex.nextS.y))\
                            or (floatLarger(c2.y - c2.x * slope, c1.y - c1.x * slope) and floatLarger(vertex.nextS.y, inters.y)):
                        break
                    vertex = vertex.nextS
            if isinstance(vertex, Vertex):
                next = vertex.next
            else:
                next = vertex.nextS
            if isinstance(vertex, Vertex):
                vertex.next = inters
            else:
                assert isinstance(vertex, Intersection)
                vertex.nextS = inters
            inters.nextS = next
            if floatEqual(c1.y, y):
                assert not floatEqual(c2.y, y)
                if floatLarger(y, c2.y):
                    inters.crossDi = 0
                else:
                    inters.crossDi = 1
            elif floatLarger(y, c1.y):
                inters.crossDi = 1
            else:
                inters.crossDi = 0

            if floatLarger(s2.x, s1.x):
                inters.crossDi = 0 if inters.crossDi == 1 else 1

            print("s1:%s, s2:%s, c1:%s, c2:%s, inter:%s, crossDi:%s" % (("%f, %f" % (s1.x, s1.y)), ("%f, %f" % (s2.x, s2.y)), ("%f, %f" % (c1.x, c1.y - c1.x * slope)), ("%f, %f" % (c2.x, c2.y - c2.x * slope)), ("%f, %f" % (inters.x, inters.y)), ("%s" % ("in" if inters.crossDi == 0 else "out"))))
            crossXs.append(inters)

    return crossXs

def processNoCross(listS, listC):
    sInC = isVertexInPolygon(listS[0], listC)
    if sInC:
        return listS
    cInS = isVertexInPolygon(listC[0], listS)
    if cInS:
        return listC
    return []

def printList(start, isS):
    assert isinstance(start, Vertex)
    next = start.next
    print("#######################################################################")
    if isS:
        print("list S:")
        print(str(start.x) + "," + str(start.y))
        while next != start:
            print(str(next.x) + "," + str(next.y))
            if isinstance(next, Vertex):
                next = next.next
            else:
                assert isinstance(next, Intersection)
                print(next.crossDi)
                next = next.nextS
    else:
        print("list C:")
        print(str(start.x) + "," + str(start.y))
        while next != start:
            print(str(next.x) + "," + str(
                next.y))
            if isinstance(next, Vertex):
                next = next.next
            else:
                assert isinstance(next, Intersection)
                print(next.crossDi)
                next = next.nextC
    print("#######################################################################")

def Compose(list):
    result = []
    for inters in list:
        assert isinstance(inters, Intersection)
        if(not inters.used) and inters.crossDi == 0:
            oneResult = []
            oneResult.append(Vertex(inters.x, inters.y))
            inters.used = True
            loopvar = inters.nextS
            print("--------------------" + str(inters.x) + "," + str(inters.y))
            while loopvar != None:
                print(str(loopvar.x) + "," + str(loopvar.y))
                oneResult.append(Vertex(loopvar.x, loopvar.y))
                if isinstance(loopvar, Intersection):
                    curr = loopvar
                    curr.used = True
                    next = curr.nextS if curr.crossDi == 0 else curr.nextC
                elif isinstance(loopvar, Vertex):
                    curr = loopvar
                    next = curr.next
                if next is inters:
                    break
                loopvar = next
            result.append(oneResult)
    for vertexs in result:
        for i in range(len(vertexs)):
            if i >= len(vertexs):
                break
            u = vertexs[i % len(vertexs)]
            v = vertexs[(i + 1) % len(vertexs)]
            if(floatEqual(u.x, v.x) and floatEqual(u.y, v.y)):
                vertexs.pop(i)
            i -= 1
    return result

def decode(lists):
    results = []
    for list in lists:
        result = ""
        for v in list:
            result += "%f %f " % (v.x, v.y)
        result = result.strip()
        results.append(result)
    return results

def encode(Str):
    myList = []
    list_float = list(map(float, Str.strip().split()))
    X = list_float[0::2]
    Y = list_float[1::2]
    assert len(X) == len(Y)
    for i in range(len(X)):
        if (not floatEqual(X[i], X[i - 1])) or (not floatEqual(Y[i], Y[i - 1])):
            myList.append(Vertex(X[i], Y[i]))
    return myList


def transDirect(list):
    newList = []
    for i in range(len(list)):
        newList.append(list[len(list) - 1 - i])
    return newList

def toClockwise(list):
    crossPr = []
    maxX = -1
    mark_i = -1

    for i in range(len(list)):
        if list[i].x > maxX:
            maxX = list[i].x
            mark_i = i
    v1 = Vertex(list[mark_i].x - list[mark_i - 1].x, list[mark_i].y - list[mark_i - 1].y)
    v2 = Vertex(list[(mark_i + 1) % len(list)].x - list[mark_i].x, list[(mark_i + 1) % len(list)].y - list[mark_i].y)
    crossPr = v1.x * v2.y - v2.x * v1.y
    while floatEqual(crossPr, 0):
        mark_i += 1
        v2 = Vertex(list[(mark_i + 1) % len(list)].x - list[mark_i % len(list)].x,
                    list[(mark_i + 1) % len(list)].y - list[mark_i % len(list)].y)
        crossPr = v1.x * v2.y - v2.x * v1.y
    assert not floatEqual(crossPr, 0)
    if crossPr < 0:
        return transDirect(list)
    else:
        return list

def PolyClipping(S, C, output_clockwise = True):
    print(S)
    print(C)
    listS = encode(S)
    listC = encode(C)
    listS = toClockwise(listS)
    listC = toClockwise(listC)
    listI = []

    for i in range(len(listS)):
        listS[i - 1].next = listS[i]
    for i in range(len(listC)):
        listC[i - 1].next = listC[i]

    for cutStartIdx in range(len(listC)):
        s1 = listC[cutStartIdx]
        s2 = listC[(cutStartIdx + 1) % len(listC)]

        inters = CutByLine(s1, s2, listS)
        if len(inters) == 0:
            continue

        if floatEqual(s1.x, s2.x):
            assert not floatEqual(s1.y, s2.y)
            if floatLarger(s2.y, s1.y):
                inters.sort(key=getY)
            else:
                inters.sort(key=getY, reverse=True)
        elif floatLarger(s2.x, s1.x):
            inters.sort(key=getX)
        else:
            inters.sort(key=getX, reverse=True)

        for v in inters:
            listI.append(v)

        s1.next = inters[0]
        for i in range(len(inters) - 1):
            inters[i].nextC = inters[i + 1]
        inters[len(inters) - 1].nextC = s2


    if len(listI) == 0:
        return decode([processNoCross(listS, listC)])

    printList(listS[0], True)
    printList(listC[0], False)

    results = Compose(listI)
    if not output_clockwise:
        results_ = []
        for result in results:
            result = transDirect(result)
            results_.append(result)
        results = results_
    return  decode(results)


S = "242 78 480 77 480 289 242 289"
C = "162 110 388 19 386 103 162 247"
point = PolyClipping(S, C)
points = point[0].split(' ')
print (points)
print (points[0])
i = 0
while i < 8:
    if i == 6:
        draw1(float(points[i]),float(points[i+1]),float(points[0]),float(points[1]))
    else:
        draw1(float(points[i]),float(points[i+1]),float(points[i+2]),float(points[i+3]))
    i = i + 2

im.show()
im1.show()

