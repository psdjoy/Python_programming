
x = int(input('Enter the number '))
r = 0
for i in range(1, x+1):
    for j in range(1, i+1):
        if i % j == 0:
            r += 1
    if r <= 2:
        print(i)
    r = 0

