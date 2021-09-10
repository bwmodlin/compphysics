import numpy as np


def get_input():
    input_size = 0
    try:
        input_size = int(input("How many fibonacci numbers do you want?: "))
    except:
        print("Please enter an integer greater than 0")
        get_input()

    if (input_size <= 0):
        print("Please enter an integer greater than 0")
        get_input()

    return input_size


fib_nums = np.array([0, 1])


def get_fib(size, fib_nums):
    if (size <= fib_nums.size):
        print(fib_nums[:(size)])

    else:
        new_num = fib_nums[-1] + fib_nums[-2]
        fib_nums = np.append(fib_nums, new_num)
        get_fib(size, fib_nums)


get_fib(get_input(), fib_nums)
