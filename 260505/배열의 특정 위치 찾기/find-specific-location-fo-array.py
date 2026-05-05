arr = list(map(int, input().split()))

sum_num = 0
avg_num = 0
cnt = 0

for i in range(len(arr)):
    if (i+1) % 2 == 0:
        sum_num += arr[i]

    if (i+1) % 3 == 0:
        avg_num += arr[i]
        cnt += 1

print(f'{sum_num} {(avg_num/cnt):.1f}')