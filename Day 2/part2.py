
f = open("input.txt", "r")

valid_count = 0

for i in f:
    letter = i[((i.find(":"))-1)]
    letter_count = 0
    i = i.split(" ")
    i[0] = i[0].split("-")
    i[0] = [(int(x))-1 for x in i[0]]

    if (i[2][(i[0][0])] == letter and i[2][(i[0][1])] != letter) or (i[2][(i[0][1])] == letter and i[2][(i[0][0])] != letter):
        valid_count += 1


print(valid_count)