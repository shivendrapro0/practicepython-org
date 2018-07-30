def isPrime(num):
    for iter in range(2, num):
        if num % iter == 0:
            return False
    return True

num = int(input("Enter a number:\t"))
if isPrime(num):
    print(num ," is  prime")
else:
    print(num , " is not prime")

