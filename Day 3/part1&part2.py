import copy
map = []
length = -1
trees_encountered = 0
with open("input.txt", "r") as f:
    map = f.read().splitlines()
map = [list(x) for x in map]
for x in map:
    length += 1
new_map = copy.deepcopy(map)
for x in range(1,100):
    for i in map:
        #print(i)
        for j in i:
            new_map[map.index(i)].append(j)
x = 0
y = 0
while y != length:
    x += 7
    y += 1
    if new_map[y][x] == ".":
        new_map[y][x] = "O"
    elif new_map[y][x] == "#":
        new_map[y][x] = "X"
        trees_encountered += 1
print(trees_encountered)