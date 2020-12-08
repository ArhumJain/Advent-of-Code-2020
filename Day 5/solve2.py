with open("input.txt", "r") as f:
    b = f.read().strip().split("\n")
ids = []
def decode(string, lowerLetter, lower, upper):
    for j in string:
        if upper != lower:
            if j == lowerLetter:
                upper = int((lower + (((upper + 1) - lower) / 2)) - 1)
            else:
                lower = int((lower + (((upper + 1) - lower) / 2)))
    return upper
for line in b:
    row = decode(line[:7], "F",0,127)
    col = decode(line[7:], "L",0,7)
    ids.append((row*8)+col)
ids.sort()
print(ids[int(len(ids)-1)])
for i in ids:
    if ids[(ids.index(i)+1)] != i + 1:
        print("My seat:", i+1)
        break
