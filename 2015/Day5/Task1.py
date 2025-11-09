def naughtyOrNice(strings):
    niceCounter = 0
    if len([i for i in strings if i in "aeiou"]) >= 3:
        niceCounter += 1
    if len([s for idx, s in enumerate(strings[:-1]) if s == strings[idx + 1]]) >= 1:
           niceCounter += 1

    if "ab" not in strings and "cd" not in strings and "pq" not in strings and "xy" not in strings:
        niceCounter += 1
    
    if niceCounter == 3:
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