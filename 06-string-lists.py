str = input("Enter a string")
rts = ""
count = len(str)

while (count>= 1):
    rts = rts + str[count-1]
    count = count -1
if rts == str:
    print(str + " string is palindrome")
else:
    print(str + " string is not palindrome")
