#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")

    loop_no = len(matrix[0]) - 1
    count = -1

    for list in matrix:
        for i in list:
            count += 1
            if count == loop_no:
                print("{}".format(i))
                count = -1
                continue
            print("{:d}".format(i), end=" ")
