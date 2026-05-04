N = int(input())
arr = list(map(float, input().split()))

total_num = 0

for i in arr:
    total_num += i

avg_num = round(total_num/N, 1)

if avg_num >= 4.0 :
    print(avg_num)
    print('Perfect')
elif 3.0 <= avg_num  < 4.0:
    print(avg_num)
    print('Good')
else:
    print(avg_num)
    print('Poor')