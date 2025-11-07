# north (^), south (v), east (>), or west (<)

# starting location => 0,0
# north => 1,0
# south => -1,0
# east => 0,1
# west => 0,-1

def uniqueHouses(cords):
    tracker = [0,0]
    uniqueList = [[0,0]]

    for i in cords:
        if i == "^":
            copy = tracker.copy()
            copy[0] += 1
            if copy not in uniqueList:
                uniqueList.append(copy)
                tracker[0] += 1
            else:
                tracker[0] += 1
        
        elif i == "v":
            copy = tracker.copy()
            copy[0] -= 1
            if copy not in uniqueList:
                uniqueList.append(copy)
                tracker[0] -= 1
            else:
                tracker[0] -= 1
        
        elif i == ">":
            copy = tracker.copy()
            copy[1] += 1
            if copy not in uniqueList:
                uniqueList.append(copy)
                tracker[1] += 1
            else:
                tracker[1] += 1
        
        elif i == "<":
            copy = tracker.copy()
            copy[1] -= 1
            if copy not in uniqueList:
                uniqueList.append(copy)
                tracker[1] -= 1
            else:
                tracker[1] -= 1
    return len(uniqueList)

with open("TestData.txt", "r") as content:
    for line in content:
        print(uniqueHouses(line))