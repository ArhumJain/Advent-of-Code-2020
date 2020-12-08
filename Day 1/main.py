report = []
with open("input.txt", "r") as f:
    report = f.readlines()
report = [int(i) for i in report]
test = [1721, 979, 366, 299, 675, 1456]
for i in report:
    for j in report:
        for x in report:
            if (i+j+x) == 2020:
                print(i*j*x)