def coordinateLightRange(brightnessMap, s):
    matrix = s.replace(",", " ").split()

    # This is for "turn on" / "turn off"
    if len(matrix) == 7:
        # matrix: ["turn", "on/off", x1, y1, "through", x2, y2]
        switch = matrix[1]      # "on" or "off"
        x1 = int(matrix[2])
        y1 = int(matrix[3])
        x2 = int(matrix[5])
        y2 = int(matrix[6])
    # For "toggle"
    else:
        # matrix: ["toggle", x1, y1, "through", x2, y2]
        switch = "toggle"
        x1 = int(matrix[1])
        y1 = int(matrix[2])
        x2 = int(matrix[4])
        y2 = int(matrix[5])

    start_y = y1  # remember original y1 so we can reset when we move x

    # We'll walk the rectangle using your while-style logic
    while x1 <= x2:
        y1 = start_y
        while y1 <= y2:
            key = f"({x1},{y1})"

            # default brightness = 0 if we haven't seen this light before
            current = brightnessMap.get(key, 0)

            if switch == "toggle":
                current += 2
            elif switch == "on":          # "turn on"
                current += 1
            elif switch == "off":         # "turn off"
                current = max(0, current - 1)

            brightnessMap[key] = current

            y1 += 1

        x1 += 1

    return brightnessMap


brightnessMap = {}

with open("TestData.txt", "r") as content:
    for line in content:
        line = line.strip()
        brightnessMap = coordinateLightRange(brightnessMap, line)

totalOutput = sum(brightnessMap.values())
print(totalOutput)
