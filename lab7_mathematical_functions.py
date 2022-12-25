"""
ECOR 1041 Lab 7 Solution Template

Author and Student Number: Olatomiwa Oladunjoye 101210403
"""

import math

#Exercise 1
def factorial(n: int) -> int:  
    """Return n! for positive values of n.  
  
    >>> factorial(1)  
    1  
    >>> factorial(2)  
    2  
    >>> factorial(3)  
    6  
    >>> factorial(4)  
    24  
    """      
    fact = 1      
    for i in range(1, n+1):  
        fact = fact * n  
     
    return fact 


x = 0
y = 0

actual = factorial(1)
print("Testing factorial(1)")
print("Expected result : 1, Actual result: ", actual)
if actual == 1:
    print("TEST PASSED")
    x +=1
else:
    print("TEST FAILED")
    y +=1

actual = factorial(2)
print("Testing factorial(2)")
print("Expected result : 2, Actual result: ", actual)
if actual == 2:
    print("TEST PASSED")
    x +=1
else:
    print("TEST FAILED")
    y +=1

actual = factorial(3)
print("Testing factorial(3)")
print("Expected result : 6, Actual result: ", actual)
if actual == 6:
    print("TEST PASSED")
    x +=1
else:
    print("TEST FAILED")
    y +=1
    
print( x , "test passed for Exercise 1")
print(y, "test failed for Exercise 1")

actual = factorial(4)
print("Testing factorial(4)")
print("Expected result : 24, Actual result: ", actual)
if actual == 24:
    print("TEST PASSED")
    x +=1
else:
    print("TEST FAILED")
    y +=1
    
print( x , "test passed for Exercise 1")
print(y, "test failed for Exercise 1")


#Exercise 2

def triangle_type(angle1: int, angle2: int, angle3: int):
    """
    The function takes three integer parameters which represents the angles in 
    a triangle, and helps to decide what type of triangle it is.
    
    >>>triangle_type( 90, 50, 40)
    This is a right angle triangle
    
    >>>triangle_type( 60, 50, 70)
    
    
    >>>triangle_type( 60, 60, 60)
    
    """
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "This is a right angle triangle"
    if angle1 > 90 or angle2 > 90 or angle3 > 90:
        return "This is an obtuse triangle"
    else: 
        return "This is an acute triangle"
x = 0
y = 0
angles = triangle_type( 90, 50, 40)
print("triangle_type( 90, 50, 40)")
print("Expected result : This is a right angle, Actual result: ", angles)
if angles == "This is a right angle triangle":
    print("Test passed")
    x +=1
else: 
    print("Test failed")
    y +=1

angles = triangle_type( 60, 60, 60)
print("triangle_type(60, 60, 60)")
print("Expected result : This is an acute triangle, Actual result: ", angles)
if angles == "This is an acute triangle":
    print("Test passed")
    x +=1
else: 
    print("Test failed")
    y +=1
    
angles = triangle_type( 95, 55, 30)
print("triangle_type( 95, 55, 30)")
print("Expected result : This is an obtuse triangle, Actual result: ", angles)
if angles == "This is an obtuse triangle":
    print("Test passed")
    x +=1
else: 
    print("Test failed")
    y +=1



angles = triangle_type( 90, 60, 30)
print("triangle_type( 95, 60, 30)")
print("Expected result : This is a ninety degree angle, Actual result: ", angles)
if angles == "This is a ninety degree angle":
    print("Test passed")
    x +=1
else: 
    print("Test failed")
    y +=1

print(x , "Test passed for Exercise 2")
print(y, "Test failed for Exercise 2")
    
#Exercise 3
def discount(customer_age: float, product_price: float):
    """
    The function takes two paramters which represents a customer's age and the 
    price of the product they wish to purchase, and returns an amount for which 
    they will have to pay based on the discount structure. The "$" represents the
    currency as a value of money.
    
    >>>customer1 = discount(14, 50)
    $0
    
    >>>customer2 = discount(23, 50)
    $2.5
    
    >>>customer3 = discount(56, 50)
    $6.5
    
    >>>customer4 = discount(69, 50)
    $8.0
    
    >>>customer5 = discount(83, 50)
    $10.0
    """
    
    x = customer_age
    y = product_price
    if  0 < x < 18:
        return "$" +  str('0')
    if 40 > x >= 18:
        return "$" + str(y * 0.05)
    if 60 > x >= 40:
        return "$" + str(y * 0.13)
    if 80 > x >= 60:
        return "$" + str(y * 0.16)
    else:
        return "$" + str(y * 0.2)

customer1 = discount(14, 50)
print(customer1)

customer2 = discount(23, 50)
print(customer2)

customer3 = discount(56, 50)
print(customer3)

customer4 = discount(69, 50)
print(customer4)

customer5 = discount(83, 50)
print(customer5)


#Exercise 4
def test_int(test_function: str, expected: int, actual: int):
    """
   Returns a result for whether the function passed or failed by taking 
   three parameters that includes the both the actual value are called.
   
   >>>test_int("factorial(1)", 1, factorial(1))
   Testing function factorial(1)
   Test passed - Expected Result: 1 Actual Result: 1
   1
   
   >>>test_int("factorial(2)", 2, factorial(2))
   Testing function factorial(2)
   Test failed Expected Result: 2 Actual Result: 4
   0
   
   >>>test_int("factorial(3)", 6, factorial(3))
   Testing function factorial(3)
   Test failed Expected Result: 6 Actual Result: 27
   0
   
   >>>test_int("factorial(4)", 24, factorial(4))
   Testing function factorial(4)
   Test failed Expected Result: 24 Actual Result: 256
   0

   """
    x = 0
    y = 0
    print("Testing function", test_function)
    pass_test = 1
    fail_test = 0    
    if actual == expected:
        print("Test passed -","Expected Result:", expected, "Actual Result:", actual)
        x += 1
        return print(pass_test)
       
    else:
        print("Test failed", "Expected Result:", expected, "Actual Result:", actual)
        y += 1
        return print(fail_test)

    
check1 = test_int("factorial(1)", 1, factorial(1)) 
check2 = test_int("factorial(2)", 2, factorial(2))
check3 = test_int("factorial(3)", 6, factorial(3))
check4 = test_int("factorial(4)", 24, factorial(4))
print(x , " is the total number of Pass")
print(y , " is the total number of Fail")
