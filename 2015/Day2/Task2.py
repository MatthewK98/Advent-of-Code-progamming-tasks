def findSurface(l,w,h):
    sideA = (2*l*w)
    sideB = (2*w*h)
    sideC = (2*h*l)
    return sideA + sideB + sideC + (min([sideA,sideB,sideC]) // 2)

def findRibbon(l,w,h):
    sides = [l,w,h]
    a = sorted(sides)[0]
    b = sorted(sides)[1]
    totalA = (a * 2) + (b * 2)
    totalB = (l * w * h)
    return totalA + totalB

total = 0
with open("TestData.txt", "r") as content:
    for line in content:
        l = int(line.split('x')[0])
        w = int(line.split('x')[1])
        h = int(line.split('x')[2])
        squareFeet = findRibbon(l,w,h)
        print(squareFeet)
        total += squareFeet
print(total)