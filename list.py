#!/usr/bin/env python3

import time
from os import system

system( "clear" )
#remove duplicates from list

#listNumbers = [ 20, 21, 22, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30, 30, 31 ]
listNumbers = [ 20, 21, 22, "if", 23, 24, 25, "if", 26, 27, 28, 29, "a", "a", 31 ]
print(listNumbers)

# I.
start_time = time.time()
listNumbers = list( set(listNumbers))         #lost the order of the elements
end_time = time.time()
total_time = end_time - start_time
print(listNumbers)
print( f"Execution time >>> {total_time}" )


# II.
from collections import OrderedDict
print( "\nII method >>>" )
my_string = "abcde"
print( f"my_string >>> {my_string}" )
list(my_string)
print( f"list(my_string) >>> {my_string}" )
listNumbers = [ 20, 21, 22, "if", 23, 24, 25, "if", 26, 27, 28, 29, "a", "a", 31 ]
print(listNumbers)
listNumber = str( listNumbers )
print( f" str >>> {listNumbers}" )







#revers a string
listNumbers = listNumbers[::-1]
print(listNumbers)

#item in list
string = "Hi there!" # True example
#string = "Good bye"  # False example
if string.find( 'Hi' ) != -1:
    print( 'Success!' )
