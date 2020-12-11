with open("input.txt", "r") as f:
    ratings = f.read().split("\n")
    ratings = [int(i) for i in ratings]
    ratings.sort()
    ratings = [0] + ratings + [ratings[int(len(ratings) - 1)] + 3]
    count = 0
    memo = {}
def arrangements(num):
    global ratings
    global count
    localcount = 0
    if num == ratings[int(len(ratings)-1)]:
        count+=1
        localcount += 1
        return localcount
    elif num in memo:
        count += memo[num]
        return memo[num]
    else:
        for i in ratings:
            if num + 1 == i or num + 2 == i or num + 3 == i:
                localcount += arrangements(i)
    if num not in memo:
        memo[num] = localcount
    return localcount
arrangements(0)
print(count)
