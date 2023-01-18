#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    count = -1
    for i in my_list:
        count += 1

    if idx < 0 or idx > count:
        return my_list

    del my_list[idx]

    return my_list
