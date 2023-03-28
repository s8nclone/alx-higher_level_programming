#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Returns:
        number of elements printed.
    """
    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            sum += 1
        except IndexError:
            break
    print()
    return (sum)
