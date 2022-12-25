"""
ECOR 1041 Lab 8

Author and Student Number: Olatomiwa Oladunjoye 101210403
"""

#Exercise 1:

RETIRED_DISCOUNT = 0.5
CHILDREN_DISCOUNT = 0.7
def ticket_price(age: int, weekend: bool)-> float:

    
    """
    The function name is ticket_price and it takes two parameters namely age in 
    int type and weekend in bool type. It returns an 
    amount that a customer should pay depending on the age bracket and the . 
    The days of week are distinguished into weekdays and weeekend, weekend is True,
    while every other entry is False.
   
    >>> x += test_str("ticket_price", "$21.0", ticket_price(10, False))
    Testing function ticket_price
    Test passed - Expected Result: $21.0 Actual Result: $21.0
    Test passed  1

    >>> x += test_str("ticket_price", "$30", ticket_price(23, False))
    Testing function ticket_price
    Test passed - Expected Result: $30 Actual Result: $30
    Test passed  2

    >>> x += test_str("ticket_price", "$21.0", ticket_price(10, False))
    Testing function ticket_price
    Test passed - Expected Result: $21.0 Actual Result: $21.0
    Test passed  3

    >>> x += test_str("ticket_price", "$20.0", ticket_price(67, True))
    Testing function ticket_price
    Test passed - Expected Result: $20.0 Actual Result: $20.0
    Test passed  4  

    >>> x += test_str("ticket_price", "$15.0", ticket_price(67, False))
    Testing function ticket_price
    Test passed - Expected Result: $15.0 Actual Result: $15.0
    Test passed  5  

    >>> x += test_str("ticket_price", "$28.0", ticket_price(10, True))
    Testing function ticket_price
    Test passed - Expected Result: $28.0 Actual Result: $28.0
    Test passed  6 
    
    >>> x += test_str("ticket_price", "$40", ticket_price(23, True))
    Testing function ticket_price
    Test passed - Expected Result: $40 Actual Result: $40
    Test passed  7

"""

    if age >= 65 and not weekend:
        return "$" + str(30 * RETIRED_DISCOUNT)
    elif age >= 65 and weekend:
        return "$" + str(40 * RETIRED_DISCOUNT) 
    elif age <= 12 and not weekend:
        return "$" + str(30 * CHILDREN_DISCOUNT)
    elif age <= 12 and weekend:
        return "$" + str(40 * CHILDREN_DISCOUNT) 
    elif (12 < age < 65) and not weekend:
        return "$" + str(30)    
    else:
        return "$" + str(40) 
    
def test_str(test_function: str, expected: str, actual: str) -> str :
    print("Testing function", test_function) 
    if actual == expected:
        print("Test passed -","Expected Result:", expected, "Actual Result:", actual)
        return 1   
    else:
        print("Test Failed -","Expected Result:", expected, "Actual Result:", actual)
        return 0
x = 0    
x += test_str("ticket_price", "$21.0", ticket_price(10, False))
print("Test passed " , x, "\n")

x += test_str("ticket_price", "$30", ticket_price(23, False))
print("Test passed " , x, " \n")

x += test_str("ticket_price", "$21.0", ticket_price(10, False))
print("Test passed " , x , " \n")

x += test_str("ticket_price", "$20.0", ticket_price(67, True))
print("Test passed " , x, " \n")

x += test_str("ticket_price", "$15.0", ticket_price(67, False))
print("Test passed " , x, " \n")

x += test_str("ticket_price", "$28.0", ticket_price(10, True))
print("Test passed " , x, " \n")

x += test_str("ticket_price", "$40", ticket_price(23, True))
print("Test passed " , x, " \n")


#Exercise 2:
T = True 
F = False
def great_42(a: int, b: int) -> bool:
    
    """
    The function great_42 takes two parameters namely 'a' and 'b' of int type and 
    returns a bool type (True or False) result if either the addition or 
    subtraction of both parameters (a , b) equals 
    42(int). 
    
    >>> y+= test_bool("great_42", True, great_42(80, 38))
    Testing function great_42
    Test passed - Expected Result: True Actual Result: True
    The number of test passed is  1 

    >>> y+= test_bool("great_42", False, great_42(145, 78))
    Testing function great_42
    Test passed - Expected Result: False Actual Result: False
    The number of test passed is  2 

    
    >>> y+= test_bool("great_42", False, great_42(2156, 56))
    Testing function great_42
    Test passed - Expected Result: False Actual Result: False
    The number of test passed is  3 
    
    >>> y+= test_bool("great_42", True, great_42(12, 30))
    Testing function great_42
    Test passed - Expected Result: True Actual Result: True
    The number of test passed is  4 

    """
    if (a + b)  == 42:
        return T
    elif  (a - b) == 42 :
        return T
    elif (b - a) == 42:
        return T
    else: return F
    
def test_bool(test_function: bool, expected: str, actual: bool) -> bool: 
    print("Testing function", test_function) 
    if actual == expected:
        print("Test passed -","Expected Result:",expected, "Actual Result:",actual)
        return 1   
    else:
        print("Test Failed -","Expected Result:",expected, "Actual Result:",actual)
        return 0        

y = 0
y+= test_bool("great_42", True, great_42(80, 38))
print("The number of test passed is ", y , "\n")

y+= test_bool("great_42", False, great_42(145, 78))
print("The number of test passed is ", y , "\n")

y+= test_bool("great_42", False, great_42(2156, 56))
print("The number of test passed is ", y , "\n")

y+= test_bool("great_42", True, great_42(12, 30))
print("The number of test passed is ", y , "\n")

print("Total passed is ",  y)


#Exercise 3
def sort_integers(a: int, b: int, c: int) ->str:

    """
    The function takes three parameters in int type form namely a, b, c and 
    returns a string with the integers sorted in ascending order.
    >>> y += test_str("sort_str", "22, 190, 809" , sort_integers(22, 809, 190))   
    Testing function sort_str
    Test passed - Expected Result: 22, 190, 809 Actual Result: 22, 190, 809

    >>> y += test_str("sort_str", "10, 19, 20" ,  sort_integers(20, 19, 10))
    Testing function sort_str
    Test passed - Expected Result: 10, 19, 20 Actual Result: 10, 19, 20

    >>> y += test_str("sort_str", "80, 96, 121", sort_integers(121, 80, 96))
    Testing function sort_str
    Test passed - Expected Result: 80, 96, 121 Actual Result: 80, 96, 121


    >>> y += test_str("sort_str", "2, 4, 9", sort_integers(2, 9, 4))
    Testing function sort_str
    Test passed - Expected Result: 2, 4, 9 Actual Result: 2, 4, 9
     
     """   
    if a < b < c:
        return str(a) + ", " + str(b) + ", " + str(c)
    elif a < c < b:
        return str(a) + ", " + str(c) + ", " + str(b)
    elif b < a < c:
        return str(b) + ", " + str(a) + ", " + str(c)
    elif b < c < a:
        return str(b) + ", " + str(c) + ", " + str(a)
    elif c < b < a:
        return str(c) + ", " + str(b) + ", " + str(a)
    elif c < a < b:
        return str(c) +", " + str(a) +", " + str(b) 

def test_str(test_function: str, expected: str, actual: str) -> str:  
    print("Testing function", test_function) 
    if actual == expected:
        print("Test passed -","Expected Result:", expected, "Actual Result:", actual)
        return 1   
    else:
        print("Test Failed -","Expected Result:", expected, "Actual Result:", actual)
        return 0

y = 0    
y += test_str("sort_str", "22, 190, 809" , sort_integers(22, 809, 190))   

y += test_str("sort_str", "10, 19, 20" ,  sort_integers(20, 19, 10)) 

y += test_str("sort_str", "80, 96, 121", sort_integers(121, 80, 96)) 

y += test_str("sort_str", "2, 4, 9", sort_integers(2, 9, 4))

print("The total number passed is" , y)

#Exercise 4
def  gross_earnings(hours_worked: float, pay_rate: float) -> str:
    """
    The function takes two parameters which represents the hours worked by an
    employee, and the pay rate of the employee. It returns the total amount
    earned by the employee on a condition of hours worked.
    
    >>> z+= test_str("gross_earnings", "$774.0", gross_earnings(42,18))
    Testing function gross_earnings
    Test passed - Expected Result: $774.0 Actual Result: $774.0

    
    >>> z+= test_str("gross_earnings", "$760", gross_earnings(40, 19))
    Testing function gross_earnings
    Test passed - Expected Result: $760 Actual Result: $760

    
    >>> z+= test_str("gross_earnings", "$660", gross_earnings(30, 22))
    Testing function gross_earnings
    Test passed - Expected Result: $660 Actual Result: $660

    
    >>> z+= test_str("gross_earnings", "$1045.0", gross_earnings(50, 19))
    Testing function gross_earnings
    Test passed - Expected Result: $1045.0 Actual Result: $1045.0
    
    """
    over_time = hours_worked - 40
    
    if hours_worked > 40:
        return "$" + str((over_time * 1.5 * pay_rate)  + ((hours_worked - over_time) * pay_rate))
    elif hours_worked <= 40:
        return "$" + str((hours_worked * pay_rate))
def test_str(test_function: str, expected: str, actual: str) -> str:
    print("Testing function", test_function)
    if actual == expected:
        print("Test passed -","Expected Result:",expected, "Actual Result:" ,actual)
        return 1
         
    else: 
        print("Test Failed")
        return 0
        
        
z = 0 
z+= test_str("gross_earnings", "$774.0", gross_earnings(42,18))

z+= test_str("gross_earnings", "$760", gross_earnings(40, 19))

z+= test_str("gross_earnings", "$660", gross_earnings(30, 22))

z+= test_str("gross_earnings", "$1045.0", gross_earnings(50, 19))

print("Number of passed is" , z) 
