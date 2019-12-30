
available = int(input('Available candy '))
x = int(input('How many candy you want '))
for i in range(1, x+1):
    if i > available:
        print('out of stock')
        break

    print('candy', i)

print('bye')