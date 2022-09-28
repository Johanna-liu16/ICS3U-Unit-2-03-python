#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Sep 2022
# This program calculates the circumference

import constants


def main():
    # this function calculates the circumference

    # input
    print("Circumference = τr")
    radius = int(input("Enter radius of a circle: "))

    # process
    circumference = constants.TAU * radius

    # output
    print("The circumference is {0} mm².".format(round(circumference, 2)))

    print("\nDone.")


if __name__ == "__main__":
    main()
