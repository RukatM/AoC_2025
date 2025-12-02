with open("data1.txt", "r") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [data[i][:1],int(data[i][1:].rstrip())]

    DialPosition = 50
    ZeroCounter = 0
    AllZeroCounter = 0

    for pair in data:
        if pair[0] == "L":
            for i in range(pair[1]):
                DialPosition -= 1
                if DialPosition== 0:
                    AllZeroCounter+=1
                elif DialPosition == -1:
                    DialPosition = 99
            if DialPosition == 0:
                ZeroCounter += 1

        elif pair[0] == "R":
            for i in range(pair[1]):
                DialPosition += 1
                if DialPosition== 100:
                    AllZeroCounter+=1
                    DialPosition = 0
            if DialPosition == 0:
                ZeroCounter += 1
print(ZeroCounter,AllZeroCounter)