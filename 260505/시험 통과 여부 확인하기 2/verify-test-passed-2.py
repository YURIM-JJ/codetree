N = int(input())

cnt = 0

for _ in range(N):
    
    arr = list(map(int, input().split()))
    sum_num = 0

    for i in arr:
        sum_num += i
    
    avg_num = sum_num/len(arr)

    if avg_num >= 60:
        cnt += 1
        print('pass')
    else:
        print('fail')

print(cnt)