

"""
ECOR 1041 Lab 6 Solution Template

Author and Student Number: Olatomiwa Oladunjoye 101210403

This file is to be used in conjunction with the detailed lab description for Lab 6
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: (../10) Single or Double Quotes - Does it matter? No it doesn't.
It depends on the expression. If for a string, it doesn't matter but if you have
a series of expression in a string, then one must follow the rule for using quotes.
You either stay consistent with either code in the expression and use the opposite 
quote for the whole expression as a string. Or you can use the \.
Ex: x = "I'm a boy"
x = 'I\'m a boy'
Both variable of x is correct as a string.
Example, "haven't" or '"Spam, spam, spam," he said.'

>>> type('Welcome To ECOR1041 Winter 2022')
# Type what you see: <class 'str'>

>>> type("Welcome To ECOR1041 Winter 2022")
# Type what you see: <class 'str'>
>>> 'Welcome'
# Type what you see: 'Welcome'

>>> ""     (An empty string - type two quotes with no spaces between them.)
# Type what you see: ''

>>> '"Hello, Welcome to Carleton University" he said.'
# Type what you see: (Nested quotations) 
'"Hello, Welcome to Carleton University" he said.'

>>> "I can't solve the mystery!" 
# Type what you see: (Nested apostrophe)
"I can't solve the mystery!"

>>> 'I can't solve the mystery!' 
# Type what you see: (Nested apostrophe)
Syntax Error: invalid syntax:<string>, line 1, pos 8

Concluding Questions: Generally, either double or single quotes works well but 
can you give a scenario where one is better than the other?
In the expression 'I can't solve the mystery!', using a double quote would have 
given a valid output. "I can't solve the mystery!"<- That expression would have 
given a valid output.

==================

Exercise 2 (../10): What operations are permitted with values of type str?

When used with strings, + is the concatenation operator. 

>>> 'Welcome ' + 'to ECOR1401'
# Type what you see: 'Welcome to ECOR1401'

When used with strings, * is the replication operator.

>>> "Welcome! " * 4
# Type what you see: 'Welcome! Welcome! Welcome! Welcome! '

>>> 4 * "Welcome! "
# Type what you see: (Reflect: What does this say about order of operators?)
'Welcome! Welcome! Welcome! Welcome! 
For string, the order of operation doesn't really matter. 

>>> "Welcome!" * 0
# Type what you see: ''

>>> "Welcome!" * -2
# Type what you see: ''

>>> "Welcome!" * "Hi!"
# Type what you see:  (Reflect: Does * work when both operators are strings?)
TypeError: can't multiply sequence by non-int of type 'str'
The * operator doesn't work as it can't multiply sequence of non-int type.

There are other operators to try now: - and /

>>> "Welcome" - "Wel"
# Type what you see: TypeError: unsupported operand type(s) for -: 'str' and 'str'

>>> 'Welcome' / 4
# Type what you see: TypeError: unsupported operand type(s) for /: 'str' and 'int'


Concluding Questions: What operators work and do not work with strings?  
Does the order of operands matter?
only the + and * operator works. The + operator works with strings only,
while the * operator works with a string and an int. The / and - operator does not 
work with strings.
=======================

Exercise 3 (../10): Understand string representation

Is  the string '123' the same as the integer 123? 
No it is not the same. 

>>> '654' + 321
# Type what you see: TypeError: can only concatenate str (not "int") to str

>>> '654' + '321'
# Type what you see: '654321'

Concluding Question: When a string looks like a number, is it a number or a string?
It is a string.
=========
Last edited: January 23, 2022
"""

#Exercise 4:
def concatenates_total_length(s1: str, s2: str) -> str:
    """ The function returns the concatenated string of the two arguments 
    (s1 and s2) and the length of the concatenated string. 
         
        >>> concatenates_total_length('Hello, ', 'world') 
        "Hello, world" has a length of 12 characters 
     
        >>> concatenates_total_length('Welcome to ', 'Canada') 
        "Welcome to Canada" has a lenght of 19
         
        >>> concatenates_total_length('ECOR', '1041') 
        "ECOR1041" has a lenght of 10
     
        >>> concatenates_total_length('', '') 
         has a lenght of 0
         
        """    
    return s1 + s2 + " has a lenght of " + str(len(s1) + len(s2))

Test_1 = concatenates_total_length("\"Mr.", "Jonah\"") 

Test_2 = concatenates_total_length("\"Boys-Guard ", "India\"")

Test_3 = concatenates_total_length("\"House on the", "Rock of Mesh\"")

Test_4 = concatenates_total_length("\" Game on the", "Mountain\"")

print(Test_1)
print(Test_2)
print(Test_3)
print(Test_4)


#Exercise 5:
def replicate(s1: str, s2: str, rep: int) -> str: 
    """  
    The function returns a string that is the result of concatenating the 
    two string arguments and replicating the concatenated string “rep” 
    times. 
 
    >>> replicate("a", "b" , 2) 
    'abab' 
    
    >>> replicate("ab" ,"c" , 2) 
    'abcabc' 
    
    >>> replicate("abc", "d", 3) 
    'abcdabcdabcd' 
    
    """
    return (s1 + s2) * rep

xin = replicate("a", "bk" , 4)
dan = replicate("ana", "maa" , 3)
abt = replicate("gboo", "gboo" , 8)
Xi = replicate("hoo", "hee" , 4)

print(xin)
print(dan)
print(abt)
print(Xi)


#Exercise 6:
def convert_to_string(num: int) -> str: 
    
    """  
    The function converts an int to a string.
    >>>  to_string(5176)
    '5176'
    
    >>>  to_string(523234)
    '523234'
    
    >>>  to_string(426)
    '426'
    
    >>>  to_string((483)
    '483'
    
    >>>  to_string(404)
    '404'
    
     >>>  to_string(404 + "sab")
     404sab
    
    """
    

    return str(num)

input1 = convert_to_string(5176)
input2 = convert_to_string(523234)
input3 = convert_to_string(426)
input4 = convert_to_string(483)
input5 = convert_to_string(404)

print(input1)
print(input2)
print(input3)
print(input4)
print(input5+ "sab")

