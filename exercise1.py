#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Rachel Lee and Ming Fu'
__email__ = "siuming.lee@mail.utoronto.ca and mm.fu@mail.utoronto.ca"

# Test case:
#input: none
#expected output: -25065.0



# define constant values
number_of_stocks = 2000
commission_rate = 0.03


# calculate the amount Lakshmi spent for 2000 stocks
stock_value = 900.00
value_purchase = number_of_stocks * stock_value


# calculate the amount Lakshmi paid her stockbroker for the purchase
commission_purchase = value_purchase * commission_rate


# calculate the amount Lakshmi made on the sale of 2000 stocks
stock_value = 942.75
value_sale = number_of_stocks * stock_value


#calculate the amount Lakshmi paid her stockbroker for the sale
commission_sale = value_sale * commission_rate


#calculate the total amount Lakshmi made (or lost) from the sale
profit = value_sale - commission_sale - value_purchase - commission_purchase

print"Lakshmi made a profit of ", profit, " dollars after the purchase and sale of 2000 stocks."
print("If Lakshmi's profit is negative, then she lost money on the transactions.")