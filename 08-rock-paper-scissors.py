def rps():
    print("Lets Play Rock Paper Scissors !! ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    input1=int(input("User A Input :"))
    input2=int(input("User B Input :"))

    if (input1 == 3 and input2 == 1) or (input1 == 1 and input2 == 2) or (input1 == 2 and input2 == 3):
        print("User B WON")
    elif input1 == input2:
        print("Both Users can't choose same")
    elif (input1 == 2 and input2 == 1) or (input1 == 3 and input2 == 2) or (input1 == 1 and input2 == 3):
        print("User A WON")
    else:
        print("Thanks for Playing !!")
        exit(0)
    rps()

rps()

