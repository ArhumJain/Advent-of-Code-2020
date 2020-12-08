count = 0
sum_of_bags = 0
class Bag():
    def __init__(self, line):
        self.name = f"{line.split()[0]} {line.split()[1]}"
        self.contains = [(f"{result.split()[1]} {result.split()[2]}", result.split()[0]) for result in
              line.split("contain ")[1].split(", ")]
        self.has_gold = False
        self.check_has_gold()
    def find_gold(self):
        global count
        global dict
        if self.has_gold == True:
            return True
        else:
            for i in self.contains:
                if i[0] != "other bags.":
                    if dict[i[0]].find_gold() == True:
                        return True
    def check_has_gold(self):
        global count
        for i in self.contains:
            if i[0] == "shiny gold":
                self.has_gold = True
    def maxBags(self):
        global sum_of_bags
        global dict
        for i in self.contains:
            if i[0] != "other bags.":
                sum_of_bags += int(i[1])
                for x in range(0,int(i[1])):
                    dict[i[0]].maxBags()
with open("input.txt", "r") as f:
    rules = f.read().split("\n")
    dict = {}
    for line in rules:
        dict[f"{line.split()[0]} {line.split()[1]}"] = Bag(line)
for i in dict:
    if dict[i].find_gold() == True:
        count += 1
dict["shiny gold"].maxBags()
print(sum_of_bags)
print(count)
