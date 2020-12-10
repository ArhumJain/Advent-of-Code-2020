with open("input.txt", "r") as f:
    pos = 1
    ratings = f.read().split("\n")
    ratings = [int(i) for i in ratings]
    ratings.sort()
    ratings = [0] + ratings + [ratings[int(len(ratings) - 1)] + 3]
    differnces = []
for i in ratings:
    if pos <= int(len(ratings)-1):
        differnces.append(ratings[pos] - ratings[pos-1])
        pos += 1
print("1 jolt:", differnces.count(1))
print("2 jolt:", differnces.count(2))
print("3 jolt:", differnces.count(3))
print("Output:",  differnces.count(1) * differnces.count(3))


