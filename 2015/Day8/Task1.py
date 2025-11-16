from string import punctuation as specialChars
def countChars(s):
    for i in s:
        if i in specialChars and i != '\x':
            s = s.remove(i)

with open ("TestData.txt", "r") as content:
    for line in content:
        print(countChars(line))