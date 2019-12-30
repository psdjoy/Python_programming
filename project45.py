
pos = -1


def totals(list, n):
    t = 0
    for i in list:
        if i == n:
            t += 1

    return t


def search(list, n):

    for i in list:
        if i == n:
            globals()['pos'] = i
            return True

    return False


arr = [5, 8, 9, 5, 9, 4, 8, 7, 9, 9, 3, 6]

n = 9

if search(arr, n):
    print("Found at", pos)

else:
    print("Not found")

print(totals(arr, n))
