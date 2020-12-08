a = []
sum = 0
with open("input.txt", "r") as f:
    a = f.read().split("\n\n")
    a = [i.replace("\n",' ') for i in a]
for i in a:
    b = []
    for j in i:
        if j not in b and j != " ":
            b.append(j)
    sum += int(len(b))
print(sum)