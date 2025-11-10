def naughtyOrNice(strings):
    niceCounter = 0
    if ([s for s in enumerate(strings) if strings.count(strings[s[0] : s[0] + 2]) > 1]):
        # print(True)
        niceCounter += 1
      
    if ([s for s in enumerate(strings[:-2]) if strings[s[0]] == strings[s[0] + 2] or strings[s[0]] == strings[s[0] + 1] and strings[s[0]] == strings[s[0] + 2]]):
        niceCounter += 1
    
    if niceCounter == 2:
        return "nice"
    
    else:
        return "naughty"


niceOutputCounter = 0
with open("TestData.txt", "r") as content:
    for line in content:
        print(naughtyOrNice(line))
        if naughtyOrNice(line) == "nice":
            niceOutputCounter += 1
    print(niceOutputCounter)