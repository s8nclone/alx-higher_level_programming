#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
            print("{:d}".format(add))


if __name__ == "__main__":

    import sys

    sum = 0
    for i in range(len(sys.arv) - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
