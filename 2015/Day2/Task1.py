def findSurface(l,w,h):
    sideA = (2*l*w)
    sideB = (2*w*h)
    sideC = (2*h*l)
    return sideA + sideB + sideC + (min([sideA,sideB,sideC]) // 2)

total = 0
with open("TestData.txt", "r") as content:
    for line in content:
        l = int(line.split('x')[0])
        w = int(line.split('x')[1])
        h = int(line.split('x')[2])
        squareFeet = findSurface(l,w,h)
        print(squareFeet)
        total += squareFeet
print(total)