N = int(input())
arr = list(map(int, input().split()))

num_lst = []

for i in arr:
    if i % 2 == 0:
        num_lst.append(i)

for j in range(len(num_lst)-1, -1, -1):
    print(num_lst[j], end=' ')