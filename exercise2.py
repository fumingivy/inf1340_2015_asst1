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
    Test 1:
    Input: 3
    Expected Output:triangle
    Actual Output: triangle

    Test 2:
    Input: 4
    Expected Output: quadrilateral
    Actual Output: quadrilateral

    Test 3:
    Input: 5
    Expected Output: pentagon
    Actual Output: pentagon

    Test 4:
    Input: 6
    Expected Output: hexagon
    Actual Output: hexagon

    Test 5:
    Input: 7
    Expected Output: heptagon
    Actual Output: heptagon

    Test 6:
    Input: 8
    Expected Output: octagon
    Actual Output: octagon

    Test 7:
    Input: 9
    Expected Output: nonagon
    Actual Output:nonagon

    Test 8:
    Input: 10
    Expected Output: decagon
    Actual Output: decagon

    Test 9:
    Input: 2
    Expected Output: Error
    Actual Output: Error

    Test 10:
    Input: 12
    Expected Output: Error
    Actual Output: Error

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

# assign a response to each expected output
    if number_of_sides == side3:
        print("triangle")
    elif number_of_sides == side4:
        print("quadrilateral")
    elif number_of_sides == side5:
        print("pentagon")
    elif number_of_sides == side6:
        print("hexagon")
    elif number_of_sides == side7:
        print("heptagon")
    elif number_of_sides == side8:
        print("octagon")
    elif number_of_sides == side9:
        print("nonagon")
    elif number_of_sides == side10:
        print("decagon")
    else:
        print("Error")

#name_that_shape()