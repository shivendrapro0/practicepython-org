list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = []
for num in list_1:
    if num<5:
        list_2.append(num)
print(list_2)
#list compression
list_2 = [num for num in list_1 if num < 5]

