import time
import random
import string

def userInput():
    # user_list = input("Enter a orderly list \t").split(',')
    # item = input("Enter a number \t")
    user_list = [ i for i in range(5,500000) if i % 5]
    item = 55340
    # print("List   : \t",user_list)
    # print("Number : \t",user_list)
    start_time = time.time()
    linearSearch(item,user_list)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    binarySearch(item,user_list)
    print("--- %s seconds ---" % (time.time() - start_time))

def linearSearch(item,user_list):
    count=0
    for i in user_list:
        if i == item:
            print(item,"Item found")
            break
        count = count + 1
    if count >= user_list.__len__():
        print(item," number not found")

def binarySearch(item,user_list):
    new_list = user_list
    while True:
        middle_count = int(new_list.__len__() / 2)
        middle_num = new_list[middle_count]
        if item == middle_num:
            print(item,"Item found")
            break
        elif new_list.__len__() == 1:
            print(item," Item not found")
            break
        elif item > middle_num:
            new_list = new_list[middle_count+1:]
        elif item < middle_num:
            new_list = new_list[:middle_count]

userInput()