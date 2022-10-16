#Please make sure you enter the beginning and the end of of your interval

n1 = int(input('Enter the begining of your interval: '))
n2 = int(input('Enter the end of your interval: '))

for num in range(n1, n2+1):
    if num > 1:
        for i in range(2, num+1):
            if num % i == 0:
                break
            else:
                print(num)
                break