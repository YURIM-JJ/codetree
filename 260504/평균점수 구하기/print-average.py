arr = list(map(float, input().split()))

sum_num = 0

for i in arr:
    sum_num += i

print(f'{sum_num/len(arr):.1f}')