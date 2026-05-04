arr = list(map(int, input().split()))

sum_num = 0
cnt = 0

for i in arr:
    if i != 0:
        cnt += 1
        sum_num += i
    else:
        break

print(f'{sum_num} {sum_num/cnt:.1f}')