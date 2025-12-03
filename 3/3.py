f = open("3.txt","r")

data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].rstrip()

sumJoltage = 0

for bank in data:
    maxJoltage = int(bank[0])
    mJIndex = 0
    for i in range(len(bank)-1):
        if int(bank[i]) > maxJoltage:
            maxJoltage = int(bank[i])
            mJIndex = i

    maxJoltage2 = int(bank[mJIndex+1])
    for i in range(mJIndex+1,len(bank)):
        if int(bank[i]) > maxJoltage2:
            maxJoltage2 = int(bank[i])

    singleBankMax = int(str(maxJoltage)+str(maxJoltage2))
    print(singleBankMax)
    sumJoltage +=singleBankMax
print(sumJoltage)

f.close()