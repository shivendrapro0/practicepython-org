def fibonacci(num):
    a = 0
    b = 1
    list_fib= [a,b]
    for i in range(1,num-1):
        c = a
        a = b
        b = c + b
        list_fib.append(b)
    return list_fib
print(fibonacci(int(input("Please entry a number"))))
