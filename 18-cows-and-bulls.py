import random,string

def getRandom(num=4):
    num_list = [ random.choice(string.digits) for i in range(0,num) ]
    return int(''.join(num_list))

def cows_n_bulls():
    cows_count = 0
    bulls_count = 0
    rand_num = getRandom(num=4)
    print("Welcome to the Cows and Bulls Game!")
    num=input("Enter a number:\n>>>")
    if int(num) <= 999:
        print("Please enter a 4 digit number")
        cows_n_bulls()
    for count in range(0,4):
        if str(rand_num) == str(num):
            print("You guess the number :)")
            exit(0)
        elif str(rand_num)[count] == str(num)[count]:
            cows_count = cows_count + 1
        elif str(num)[count] in str(rand_num):
            bulls_count = bulls_count + 1
        else:
            print("Exit")
    print(cows_count, "cows , ",bulls_count, " bulls" )
    cows_n_bulls()

if __name__ == "__main__":
    cows_n_bulls()
