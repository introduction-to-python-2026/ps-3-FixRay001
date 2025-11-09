def move(my_list, direction):
    new_list = my_list.copy()
    index_of_one = new_list.index(1)

    if direction == "right" and index_of_one < len(new_list) - 1:
        new_list[index_of_one], new_list[index_of_one + 1] = 0, 1
    elif direction == "left" and index_of_one > 0:
        new_list[index_of_one], new_list[index_of_one - 1] = 0, 1

    return new_list    
