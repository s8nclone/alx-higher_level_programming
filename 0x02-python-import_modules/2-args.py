#!/usr/bin/python3
if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print("{:d} argument:".format(num))
        return
    else:
        if num == 1:
            print("{:d} argument:".format(num))
        else:
            print("{:d} arguments:".format(num))
        i = 1
        while i <= num:
            print("{:d}: {:s}".format(i, arv[i]))
            i += 1

    if __name__ == "__main__":
        import sys
        print_arg(sys.argv)
