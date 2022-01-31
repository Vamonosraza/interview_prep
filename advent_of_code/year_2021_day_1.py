with open("year_2021_day_1.txt") as f:
    data = [int(i) for i in f.read().strip().split("\n")]


    n = len(data)
    count = 0 
    for i in range(1, n):
        if data[i] > data [i - 1]:
            count += 1

print(count)
