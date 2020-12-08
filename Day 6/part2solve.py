from collections import Counter
a = []
sum = 0
with open("input.txt", "r") as f:
    a = f.read().split("\n\n")
    a = [i.split("\n") for i in a]
for i in a:
    counter = []
    for j in i:
        for x in j:
            counter.append(x)
    counter = Counter(counter)
    for x in counter.items():
        if x[1] == int(len(i)):
            sum+=1
print(sum)