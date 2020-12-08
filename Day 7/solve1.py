bag = "shiny gold bag"
count = 0
with open("input.txt", "r") as f:
    rules = f.read().split(".\n")
    rules = [i.split("contain") for i in rules]
    rulesDict = {}
    for i in rules:
        rulesDict[i[0]] = i[1]
def recur(x):
    returnCount = 0
    if rulesDict[x] != " no other bags":
        if bag in rulesDict[x]:
            returnCount += 1
        else:
            for i in rulesDict:
                if (i.rstrip(" ").rstrip("s") in rulesDict[x]):
                    if bag in rulesDict[i]:
                        returnCount += 1
                        break
                    else:
                        recur(i)
    return returnCount
for x in rulesDict:
    count += recur(x)
print(count)
