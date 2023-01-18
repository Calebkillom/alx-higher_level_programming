#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if args == 0:
        print("{} arguments.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(args))
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print("{}: {}".format(i, arg))
