with open("input.txt", "r") as f:
    data = f.read().split("\n")
    preamble = 25
    pos = 25
    print(data)
def decrypt(num, maxSum):
    global data
    numbers = []
    dPos = data.index(str(num))
    sum = 0
    while sum < maxSum:
        sum+=int(data[dPos])
        numbers.append(int(data[dPos]))
        dPos+=1
    numbers.sort()
    if sum == maxSum:
        return (numbers[0] + numbers[int(len(numbers)-1)])
    else:
        return None
while True:
    prevPos = pos
    for i in range(pos-preamble, pos):
        for j in range(pos-preamble, pos):
            if int(data[i])+int(data[j]) == int(data[pos]):
                pos+=1
                break
    if prevPos == pos:
        break
for i in data:
    check = decrypt(int(i), int(data[pos]))
    if check != None:
        print(check)
        break