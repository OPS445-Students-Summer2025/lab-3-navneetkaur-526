#!/usr/bin/env python3

# Global list declared outside any function
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Return all items in the list
    return my_list

def give_first_item():
    # Return the first item
    return str(my_list[0])
def give_first_and_last_item():
    # Return a list of the first and last items
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Return a list of the second and third items
    return [my_list[1], my_list[2]]

if __name__ == '__main__':
    print(give_list())                  # [100, 200, 300, 'six hundred']
    print(give_first_item())           # 100
    print(give_first_and_last_item()) # [100, 'six hundred']
    print(give_second_and_third_item())# [200, 300]
