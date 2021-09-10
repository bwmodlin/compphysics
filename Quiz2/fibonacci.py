import numpy as np
import matplotlib.pyplot as plt


def get_input():
    input_size = 0
    try:
        input_size = int(input(
            "How many fibonacci numbers do you want? (overflows a little bigger than n=90): "))
    except:
        print("Please enter an integer greater than 0")
        get_input()

    if (input_size <= 0):
        print("Please enter an integer greater than 0")
        get_input()

    return input_size


fib_nums = np.array([0, 1])


def get_fib(size):
    global fib_nums
    if (size <= fib_nums.size):
        print("Fibonacci sequence array: \n")
        print(fib_nums[:(size)])

    else:
        new_num = fib_nums[-1] + fib_nums[-2]
        fib_nums = np.append(fib_nums, new_num)
        get_fib(size)


get_fib(get_input())


if (fib_nums.size > 2):
    ratio_nums = np.array([])
    for num in range(2, fib_nums.size):
        print(num)
        new_ratio = fib_nums[num] / fib_nums[num-1]
        ratio_nums = np.append(ratio_nums, new_ratio)

    print("Approximating golden ratio array: \n")
    print(ratio_nums)

    n_values = np.arange(3, fib_nums.size+1)
    plt.plot(n_values, ratio_nums)
    plt.xlabel("Size of fibonacci sequence (n)")
    plt.ylabel("Golden Ratio Estimate")
    plt.title("Estimating Golden Ratio over the Fibonacci Sequence")
    plt.show()
