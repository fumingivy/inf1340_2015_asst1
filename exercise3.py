#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Rachel Lee and Ming Fu'
__email__ = "siuming.lee@mail.utoronto.ca and mm.fu@mail.utoronto.ca"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """
    answer = raw_input("Is the car silent when you turn the key? (Y/N)")

    if answer == "Y":
        print("Are the battery terminals corroded?")
        if answer == "Y":
            print("The battery terminals are corroded. Clean terminals and try starting again.")
        elif answer == "N":
            print("The battery cables may be damaged.Replace cables and try again.")
    elif answer == "N":
        print("Does the car make a clicking noise?")
        if answer == "Y":
            print("Battery is not work correctly. Replace the battery.")
        elif answer == "N":
            print("Does the car crank up but fail to start?")
            if answer == "Y":
                print("Check spark plug connections.")
            elif answer == "N":
                print("Does the engine start and then die?")
                if answer == "Y":
                    print("Does your car have fuel injection?")
                    if answer == "Y":
                        print("Your car needs to be fix. Get it in for service.")
                    elif answer == "N":
                        print("Check to ensure the choke is opening and closing.")
                else:
                    print("Engine is not getting enough fuel. Clean fuel pump.")


diagnose_car()