#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program generates a random number and makes the user
# keep guessing until they get it

import random


def main():
    # This function generates a random number and makes the user
    # keep guessing until they get it

    print("")
    print("This program generates a number, from 0 to 9, and "
          "makes the user guess it over and over until they get it")
    print("")
    generated_number = random.randint(0, 9)

    while(True):
        number_str = input("What is your guess: ")
        try:
            number = int(number_str)
        except Exception:
            print("This was not an integer")
        else:
            if generated_number == number:
                print("That Guessed Correctly")
                break
            else:
                print("Sorry, Try Again")
        print("")


if __name__ == "__main__":
    main()
