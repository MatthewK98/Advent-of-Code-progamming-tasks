with open('TestData.txt', 'r') as content:
    total = 0
    for line in content:
        for character in line:
            if character == "(":
                total += 1
            elif character == ")":
                total -= 1
        print(total)