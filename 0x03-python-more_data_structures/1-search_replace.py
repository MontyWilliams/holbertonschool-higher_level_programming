#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newList = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            newList.insert(i, replace)
        else:
            newList.insert(i, my_list[i])
    return newList
