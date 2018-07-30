num = int(input("Please enter a Number"))

list_d = []
for n in range(2,num+1):
    if num%n == 0:
        list_d.append(n)

print(list_d)
