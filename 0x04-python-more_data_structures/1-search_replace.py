#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    return ([new_list = replace for i in range(len(new_list)) if search in new_list])
