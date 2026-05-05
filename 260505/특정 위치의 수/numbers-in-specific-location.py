arr = list(map(int, input().split()))

sum_num = 0

for i in range(10):
    if i == 2 or i == 4 or i == 9:
        sum_num += arr[i]

print(sum_num)