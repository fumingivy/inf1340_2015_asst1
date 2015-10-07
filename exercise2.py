#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Rachel Lee and Ming Fu'
__email__ = "siuming.lee@mail.utoronto.ca and mm.fu@mail.utoronto.ca"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """
# name the input
    number_of_sides = raw_input("Enter the number of sides from 3 to 10:")

    side3 = "3"
    side4 = "4"
    side5 = "5"
    side6 = "6"
    side7 = "7"
    side8 = "8"
    side9 = "9"
    side10 = "10"

# name the expected output
    if number_of_sides == side3:
        print("Triangle")
    elif number_of_sides == side4:
        print("Quadrilateral")
    elif number_of_sides == side5:
        print("Pentagon")
    elif number_of_sides == side6:
        print("Hexagon")
    elif number_of_sides == side7:
        print("Heptagon")
    elif number_of_sides == side8:
        print("Octagon")
    elif number_of_sides == side9:
        print("Nonagon")
    elif number_of_sides == side10:
        print("Decagon")
    else:
        print("Error")

name_that_shape()