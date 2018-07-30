import random
NUM_I=1
NUM_L=9

while True:
    print("Type 'exit' to quit application")
    random_number=random.randint(NUM_I,NUM_L+1)
    num =input("Guess a Number Shriman :) :\t")
    if num == 'exit':
        print("exiting now")
        break
    if int(num) > random_number:
        print("You guess too high ", random_number)
    elif int(num) < random_number:
        print("You guess to low", random_number)
    elif int(num) == random_number:
        print("Wow" , random_number)
