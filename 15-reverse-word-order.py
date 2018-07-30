long_string = input("Please enter a sentence:\t")
long_string_list = long_string.split()
str_len = long_string_list.__len__()
newstr = ""
while str_len >= 1:
    newstr = newstr + " " + long_string_list[str_len-1]
    str_len = str_len - 1

print(newstr)
