with open('TestData.txt', 'r') as content:
    total = 0
    pos = 0
    for line in content:
        for character in line:
            if total == -1:
                print(pos)
                break
            elif character == "(":
                total += 1
                pos += 1
            elif character == ")":
                total -= 1
                pos += 1