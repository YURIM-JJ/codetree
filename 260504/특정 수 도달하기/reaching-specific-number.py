arr = list(map(int, input().split()))

num = 0
cnt = 0

for i in arr:
    if i < 250:
        cnt += 1
        num += i  
    else:
        break

print(f'{num} {num/cnt:.1f}')