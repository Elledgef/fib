# Author: Faith Elledge
# Grithub username: Elledgef
# Date: 4/20
# Description: This code will take positive integer parameter and returns number
# at that position of the Fibonacci sequence

def fib(num_terms):
    """ Function takes positive integer parameter and returns number
     at that position of the Fibonacci sequence """
    #first two numbers in fibonnaci series
    num_1,num_2 = 1,1
    #count starts at 0
    count = 0
    #loop
    while count < num_terms
        term = num_1
        num_3 = num_1 + num_2
        #reassign
        num_1 = num_2
        num_2 = num_3
        #count
        count += 1
    return term
