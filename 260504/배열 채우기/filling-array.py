arr = list(map(int, input().split()))

num_list = []

for i in arr:
    if i != 0:
        num_list.append(i)
    else:
        break

for j in range(len(num_list)-1,-1,-1):
    print(num_list[j], end=' ')