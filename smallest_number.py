#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on June 2021
# This program determines the smallest of 10 random numbers

import random


def determine_smallest(numbers):
    # this function determines the smallest number

    smallest = numbers[0]

    for counter in numbers:
        if counter < smallest:
            smallest = counter

    return smallest


def main():
    # this function generates the random numbers

    numbers = []

    # process
    print("Generating random numbers...")
    print("")
    for loop_counter in range(0, 10):
        generated_number = random.randint(1, 100)
        numbers.append(generated_number)
        print("Number {0} is {1}.".format(loop_counter + 1,
                                          numbers[loop_counter]))
    # call functions
    smallest_number = determine_smallest(numbers)
    # output
    print("\nThe smallest number is {}.".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
