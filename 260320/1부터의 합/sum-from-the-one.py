N = int(input())
cnt = 0
idx = 0

for i in range(1, 101):
    cnt += i
    if cnt >= N:
        idx = i
        break

print(idx)