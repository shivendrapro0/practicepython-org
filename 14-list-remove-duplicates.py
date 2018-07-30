def removeduplicateElementList1():
    user_input_list = input("Enter list").split(',')
    new_list = set(user_input_list) & set(user_input_list)
    print(new_list)

def removeDuplicateElementList2():
    user_input_list = input("Enter list").split(',')
    new_list = []
    for element in user_input_list:
        if element not in new_list:
            new_list.append(element)
    print(new_list)
