#!/usr/bin/python3
def element_at(my_list, id):
    if id < 0:
        return None
    elif id >= len(my_list):
        return None
    else:
        return my_list[id]
