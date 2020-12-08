
batch1 = []
batch2 = []
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validFields = 0
validPassports = 0
with open("input.txt", "r") as f:
    batch1 = f.read()
    batch1 = batch1.split("\n\n")
for x in batch1:
    if all(i in x for i in fields):
        batch2.append(x)
        validFields += 1
for x in batch2:
    batch2[batch2.index(x)] = x.replace("\n", " ")
for x in batch2:
    batch2[batch2.index(x)] = x.split(" ")

for i in batch2:
    passedFields = 0
    keys = []
    keyValues = []
    pass_dict = {}
    for j in i:
        j = j.split(":")
        keys.append(j[0])
        keyValues.append(j[1])
    pass_dict = dict(zip(keys, keyValues))
    if (int(pass_dict["byr"]) >= 1920) and (int(pass_dict["byr"]) <= 2002):
        passedFields += 1
    if (int(pass_dict["iyr"]) >= 2010) and (int(pass_dict["iyr"]) <= 2020):
        passedFields += 1
    if (int(pass_dict["eyr"]) >= 2020) and (int(pass_dict["eyr"]) <= 2030):
        passedFields += 1
    if "cm" in pass_dict["hgt"]:
        if len(pass_dict["hgt"]) == 5:
            if pass_dict["hgt"][3:6] == "cm":
                try:
                    if (int(pass_dict["hgt"][0:3]) >= 150) and (int(pass_dict["hgt"][0:3]) <= 193):
                        passedFields += 1
                except:
                    break
    if "in" in pass_dict["hgt"]:
        if len(pass_dict["hgt"]) == 4:
            if pass_dict["hgt"][2:5] == "in":
                try:
                    if (int(pass_dict["hgt"][0:2]) >= 59) and (int(pass_dict["hgt"][0:2]) <= 76):
                        passedFields += 1
                except:
                    break

    if pass_dict["hcl"][0] == "#" and len(pass_dict["hcl"]) == 7:
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        char = ["a", "b", "c", "d", "e", "f"]
        for i in pass_dict["hcl"][1:7]:
            if (i not in char) and (i not in num):
                break
            else:
                if i == pass_dict["hcl"][6]:
                    passedFields += 1
                    break
                continue

    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if pass_dict["ecl"] in ecl:
        passedFields += 1

    try:
        if (int(pass_dict["pid"]) >= 1) and (int(pass_dict["pid"]) <= 999999999):
            passedFields += 1
    except:
        continue


    if passedFields == 7:
        validPassports += 1


    print(pass_dict)


print(validPassports)

