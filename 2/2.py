def isInvalid(number):
    if len(number) % 2 == 1:
        return False

    middleElement = len(number) // 2
    if number[:middleElement] == number[middleElement:]:
        return True

    return False

def InvalidPart2Partial(start,end):
    invalids = []

    for candidate in range(start,end + 1):
        for i in range(len(str(candidate))):
            repeats = len(str(candidate)) // len(str(candidate)[:i+1])
            if repeats > 1:
                if str(candidate)[:i+1] * repeats == str(candidate):
                    # print(str(candidate)[:i+1], len(str(candidate)), len(str(candidate)[:i+1]), str(candidate))
                    if candidate not in invalids:
                        invalids.append(candidate)
    return invalids

file = open("data2.txt", "r")
data = file.readline().split(",")
for i in range(len(data)):
    data[i] = data[i].split("-")

sumOfInvalids = 0

#part1
# for pair in data:
#     for number in range(int(pair[0]),int(pair[1])+1):
#         if isInvalid(str(number)):
#             sumOfInvalids += number


#part2
for pair in data:
    sumOfInvalids += sum(InvalidPart2Partial(int(pair[0]),int(pair[1])))
print(sumOfInvalids)

file.close()