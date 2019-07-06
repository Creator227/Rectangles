import sys
import math
fin = open("RectanglesIN.txt", "r")
sys.stdout = open("rect.out", "w")

Xmax, Ymax, N = map(int, fin.readline().split())
rectangles = list()
lines = list()
for string in fin.readlines():
    xleft, yright, xright, yleft = map(int, string.split())
    tgmin = yright / xright
    if xleft:
        tgmax = yleft / xleft
    else:
        tgmax = Ymax
    lines.append(tgmin)
    rectangles.append((tgmin, tgmax))

best_line = float()
best_crossing = int()

rectangles.sort(key = lambda x: x[0])
lines.sort()
for line in lines:
    cross_num = int()
    for rectangle in rectangles:
        if line >= rectangle[0] and line <= rectangle[1]:
            cross_num += 1
        elif line < rectangle[0]:
            break

    if cross_num > best_crossing:
        best_crossing = cross_num
        best_line = line

if best_line >= Ymax/Xmax:
    print(best_crossing, math.ceil(Ymax / best_line), Ymax)
else:
    print(best_crossing, Xmax, int(Xmax * best_line))