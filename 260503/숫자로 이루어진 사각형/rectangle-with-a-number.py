def num_square(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num, end=' ')
            num += 1

            if num == 10:
                num = 1
        
        print()


num_square(int(input()))