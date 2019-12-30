pos = -1


def search(list, n):

    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (u + l)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


arr = [4, 7, 8, 12, 45, 78, 99]
n = 99

if search(arr, n):
    print("Found at", pos)

else:
    print("Not found")
