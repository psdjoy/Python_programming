from functools import reduce

nums = [2, 3, 4, 5, 6, 7, 8, 9, 32, 89, 50]

evens = list(filter(lambda n: n % 2 == 0, nums))

print(evens)
doubles = list(map(lambda n: n * 2, evens))
print(doubles)

sums = reduce(lambda a, b: a + b, doubles)
print(sums)
