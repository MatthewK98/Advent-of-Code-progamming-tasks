# This will create the Dictionary for every coordinate
mapCoordinates = {}
x1 = 0
y1 = 0
x2 = 999
y2 = 999
tmp = y1

while y1 <= y2:
    # print("[ " + str(x1) + ", " + str(y1) + " ]")
    key = "(" + str(x1) + "," + str(y1) + ")"
    mapCoordinates[key] = "off"
    y1 += 1
    
    if y1 > y2:
        x1 += 1
        y1 = tmp
    
    if x1 > x2:
        break

def coordinateLightRange(mapCoordinates, s):
    # print(mapCoordinates)
    matrix = s.replace(","," ").split()

    # This is for on or off
    if len(matrix) == 7:
        switch = matrix[1]
        x1 = int(matrix[2][0:])
        y1 = int(matrix[3][0:])
        x2 = int(matrix[5][0:])
        y2 = int(matrix[6][0:])
    
    # For Toggle
    else:
        switch = matrix[0]
        x1 = int(matrix[1][0:])
        y1 = int(matrix[2][0:])
        x2 = int(matrix[4][0:])
        y2 = int(matrix[5][0:])

    count = 0
    tmp = y1
    while y1 <= y2:
        key = "(" + str(x1) + "," + str(y1) + ")"
        if switch == "toggle":
            if mapCoordinates[key] == "off":
                mapCoordinates[key] = "on"
            else:
                mapCoordinates[key] = "off"


        if switch != "toggle":
            mapCoordinates[key] = switch
        
        
        y1 += 1
        count += 1
        
        if y1 > y2:
            x1 += 1
            y1 = tmp
        
        if x1 > x2:
            return mapCoordinates
            
totalOutput = 0
with open("TestData.txt", "r") as content:
    for line in content:
        info = coordinateLightRange(mapCoordinates, line)
        onCount = list(info.values()).count("on")
        # print(info)
        
        # print(onCount)
    print(list(info.values()).count("on"))