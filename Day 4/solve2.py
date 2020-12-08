import re

def parse(file):
    batch = []
    with open(file, "r") as f:
        batch = f.read()
        batch = batch.split("\n\n")
    for x in batch:
        batch[batch.index(x)] = x.replace("\n", " ")
    return batch

def fieldParse(batch):
    fieldList = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validCount = 0
    filteredBatch = []
    for i in batch:
        fields = re.findall(r'[a-z]{3}(?=:)', i)
        if all(j in i for j in fieldList):
            filteredBatch.append(i)
            validCount += 1
    return filteredBatch

def validate(batch):
    new_batch = []
    validPassports = 0
    for i in batch:
        keys = re.findall(r'[a-z]{3}(?=:)', i)

        values = re.findall(r'[^:][a-z0-9#-)]*(?=\s)|(?=\s\s)', i)
        if "cid" in keys:
            try:
                values.pop(keys.index("cid"))
            except:
                continue
            keys.pop(keys.index("cid"))
        print(keys)
        print(values)
        i = dict(zip(keys,values))
        new_batch.append(i)

    print(new_batch)
    for i in new_batch:
        passedFields = 0

        if (int(i["byr"]) >= 1920) and (int(i["byr"]) <= 2002):
            passedFields += 1
        if (int(i["iyr"]) >= 2010) and (int(i["iyr"]) <= 2020):
            passedFields += 1
        if (int(i["eyr"]) >= 2020) and (int(i["eyr"]) <= 2030):
            passedFields += 1
        if "cm" in i["hgt"]:
            if len(i["hgt"]) == 5:
                if i["hgt"][3:6] == "cm":
                    try:
                        if (int(i["hgt"][0:3]) >= 150) and (int(i["hgt"][0:3]) <= 193):
                            passedFields += 1
                    except:
                        break
        if "in" in i["hgt"]:
            if len(i["hgt"]) == 4:
                if i["hgt"][2:5] == "in":
                    try:
                        if (int(i["hgt"][0:2]) >= 59) and (int(i["hgt"][0:2]) <= 76):
                            passedFields += 1
                    except:
                        break

        if i["hcl"][0] == "#" and len(i["hcl"]) == 7:
            num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            char = ["a", "b", "c", "d", "e", "f"]
            for i in i["hcl"][1:7]:
                if (i not in char) and (i not in num):
                    break
                else:
                    if i == i["hcl"][6]:
                        passedFields += 1
                        break
                    continue

        ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if i["ecl"] in ecl:
            passedFields += 1

        try:
            if (int(i["pid"]) >= 1) and (int(i["pid"]) <= 999999999):
                passedFields += 1
        except:
            continue

        if passedFields == 7:
            validPassports += 1

        #rint(i)
    return validPassports
batch = parse("input.txt")

batch = fieldParse(batch)
print(batch)
batch = validate(batch)
print(batch)

