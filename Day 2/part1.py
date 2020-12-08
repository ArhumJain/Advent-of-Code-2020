
f = open("input.txt", "r")

valid_count = 0

for i in f:
    letter = i[((i.find(":"))-1)]
    letter_count = 0
    i = i.split(" ")
    i[0] = i[0].split("-")
    i[0] = [int(x) for x in i[0]]
    for j in i[2]:
        if j == letter:
            letter_count += 1
    if (letter_count >= i[0][0]) and (letter_count <= i[0][1]):
        valid_count += 1
f.close()
print(valid_count)


