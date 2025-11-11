#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/30/2025
# Program to ask the user for an integer


def main():
    # get user input and handle exceptions
    user_num = input("Please enter an integer: ")
    try:
        user_num = int(user_num)
        if user_num < 0:
            print("Please enter a positive integer.")
        else:
            counter = 0
            sum = 0
            while counter <= user_num:
                sum += counter
                counter += 1
            print("The sum of the numbers from 0 to", user_num, "is", sum)
    except ValueError:
        print(user_num, "is not an integer.")
    # display ending message to user no matter the outcome
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
