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

Test 1:
    Inputs: Y, Y
    Expected Outputs: Clean terminals and try starting again
    Actual Output:Clean terminals and try starting again

Test 2:
    Inputs: Y, N
    Expected Outputs: Replace cables and try again.
    Actual Outputs: Replace cables and try again.

Test 3:
    Inputs: N, Y
    Expected Outputs: Replace the battery.
    Actual Output; Replace the battery.

Test 4:
    Inputs: N, N, Y
    Expected Outputs: Check spark plug connections.
    Actual Output: Check spark plug connections.

Test 5:
    Inputs: N, N, N, N
    Expected Outputs: Engine is not getting enough fuel. Clean fuel pump.
    Actual Output: Engine is not getting enough fuel. Clean fuel pump.

Test 6:
    Inputs: N, N, N, Y, N
    Expected Outputs: Check to ensure the choke is opening and closing.
    Actual Output: Check to ensure the choke is opening and closing.

Test 7:
    Inputs: N, N, N, Y, Y
    Expected Outputs: Get it in for service.
    Actual Output: Get it in for service.
    """

    # program codes following the decision tree:

    answer = raw_input("Is the car silent when you turn the key? (Y/N)")
    if answer == "Y":
        answer = raw_input("Are the battery terminals corroded?(Y/N)")
        if answer == "Y":
            print("Clean terminals and try starting again.")
        elif answer == "N":
            print("Replace cables and try again.")

    elif answer == "N":
        answer = raw_input("Does the car make a clicking noise?(Y/N)")
        if answer == "Y":
            print("Replace the battery.")
        elif answer == "N":
            answer = raw_input("Does the car crank up but fail to start?")
            if answer == "Y":
                print("Check spark plug connections.")
            elif answer == "N":
                answer = raw_input("Does the engine start and then die?")
                if answer == "N":
                    print("Engine is not getting enough fuel. Clean fuel pump.")
                elif answer == "Y":
                    answer = raw_input("Does your car have fuel injection?")
                    if answer == "N":
                        print("Check to ensure the choke is opening and closing.")
                    elif answer == "Y":
                        print("Get it in for service.")

#diagnose_car()