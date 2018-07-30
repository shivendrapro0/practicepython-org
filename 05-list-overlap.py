a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

union = set(a) & set(b)
print(type(union))

import random
a = random.sample(range(30),15)
b = random.sample(range(30),10)

union = set(a) & set(b)
print("A = ", a)
print("B = ", b)
print("Union = ",union)
