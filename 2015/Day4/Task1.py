import hashlib

s = "ckczppom"

i = 000000
while i < 9999999:
    scopy = s + str(i)
    res = hashlib.md5(scopy.encode())
    hexAnswer = res.hexdigest()

    if hexAnswer[:6] == "000000":
        print(scopy)
        print(hexAnswer)
        break
    
    else:
        i += 1