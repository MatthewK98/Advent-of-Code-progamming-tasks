def bitwiseLogicGate(input):
    line = input.split("->")
    assign = line[-1][1]
    wires = {}

    try:
        num = int(line[0])
        wires[assign] = num

    except ValueError:
        



    return wires
    
    



with open("TestData.txt", "r") as content:
    for line in content:
        print(bitwiseLogicGate(line.strip()))