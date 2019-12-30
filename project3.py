x = 4
r = x % 2
if r == 0:
    print('even')
    if x > 2:
        print('great')
    elif x < 2:
        print('not great')
    else:
        print('oh no')

else:
    print('odd')
