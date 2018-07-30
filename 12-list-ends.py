def listfunction():
    enter_list = input("Enter list :\t")
    new_list = [enter_list.split(',')[0],enter_list.split(',')[enter_list.split(',').__len__()-1]]
    print(new_list)
listfunction()

