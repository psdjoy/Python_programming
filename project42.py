
a = 5
b = 0
try:
    print("resource open")
    print(a/b)
    k = int(input("Put a number "))
    print(k)

except ZeroDivisionError as e:
    print("Not divided by zero", e)

except ValueError as e:
    print("Invalid number ")

except Exception as e:
    print("something wrong")

finally:
    print("closed")

print("bye")
