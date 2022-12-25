"""
ECOR 1041 Lab 10

Author and Student Number: Olatomiwa Oladunjoye 101210403
"""
#Exercise 1
def Fibonacci_sequence(n : int) -> list:
    """
    The function  takes  one parameter named n of an int type. The  function  
    returns  a  list  containing the  Fibonacci  sequence  until the nth term.
    The Fibonacci sequence is defined as  Fn =  Fn-1 + Fn-2.
    
    >>> y += test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5]" , Fibonacci_sequence(6))
    Test Passed - Expected Result: [0, 1, 1, 2, 3, 5] Actual Result: [0, 1, 1, 2, 3, 5]
    
    >>> y += test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5, 8]" , Fibonacci_sequence(7))
    Test Passed - Expected Result: [0, 1, 1, 2, 3, 5, 8] Actual Result: [0, 1, 1, 2, 3, 5, 8]   

    
    >>> y += test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5, 8, 13]" , Fibonacci_sequence(8))
    Test Passed - Expected Result: [0, 1, 1, 2, 3, 5, 8, 13] Actual Result: [0, 1, 1, 2, 3, 5, 8, 13]      

    
    >>> y += test_list("Fibonacci_sequence", "[0, 1, 1, 2]" , Fibonacci_sequence(4))
    Test Passed - Expected Result: [0, 1, 1, 2] Actual Result: [0, 1, 1, 2]  
    
    """ 
    
    fibonacci = [0, 1]
    if n <= 0:
        return 0
    for i in range(2, n):
        new_element = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci+=[new_element]    
    return str(fibonacci)
def test_list(test_function: str, expected: str, actual: str) -> str:  
    print("Testing function", test_function) 
    if actual == expected:
        print("Test passed -","Expected Result:", expected, "Actual Result:", actual)
        return 1   
    else:
        print("Test Failed -","Expected Result:", expected, "Actual Result:", actual)
        return 0

y = 0    
y += test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5]" , Fibonacci_sequence(6))
y += test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5, 8]" , Fibonacci_sequence(7))
y += test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5, 8, 13]" , Fibonacci_sequence(8))
y += test_list("Fibonacci_sequence", "[0, 1, 1, 2]" , Fibonacci_sequence(4))

print("The total number passed is", y)

print("\n")


#Exercise 2
def max_min():
    """
    The function returns the largest and smallest elements as a list 
    after prompting the user to enter an integer until the user enters zero.
    """
    x = input("Please enter an integer (enter zero to quit): " )
    biggest_lowest = []
    
    while x != str(0) :
        biggest_lowest+=[int(x)]
        x = input("Please enter an integer (enter zero to quit):")
        
    biggest = biggest_lowest[0]   
    lowest = biggest_lowest[0]
    for item in range(1, len(biggest_lowest)):
        if biggest < biggest_lowest[item]:
            biggest = biggest_lowest[item]
        if lowest > biggest_lowest[item]:
            lowest = biggest_lowest[item]
            
    return 'The list = ' + str(biggest_lowest) + ', max = ' + str(biggest) + ', min = ' + str(lowest)
print(max_min())

print("\n")


#Exercise 3
def max_occurrences(squad_list: list) -> int:
    """
    The function takes one parameter in list type. It returns  the value with the maximum 
     number of occurrences in the given list.
     
     >>> b+=test_list("max_occurrences", "4" , max_occurrences([4,66,4,7, 8,9, 0,2,4,7,]))
     Testing function max_occurrences
     Test passed - Expected Result: 4 Actual Result: 4

     >>> b+=test_list("max_occurrences", "66" , max_occurrences([4,66,4,66, 8,66, 0,2]))
     Testing function max_occurrences
     Test passed - Expected Result: 66 Actual Result: 66

     >>> b+=test_list("max_occurrences", "7" , max_occurrences([7,66,4,7, 8,9, 7,2,4,7,]))
     Testing function max_occurrences
     Test passed - Expected Result: 7 Actual Result: 7

     >>> b+=test_list("max_occurrences", "0" , max_occurrences([4,0,4,7, 0,9, 0,2,0,7,]))
     Testing function max_occurrences
     Test passed - Expected Result: 0 Actual Result: 0
    """

    squad_numbers = []
    for i in squad_list:
        if i not in squad_numbers:
            squad_numbers+=[i]

    Table = []
    for i in squad_numbers:
        count = 0 
        for j in squad_list:
            if i == j:
                count+=1
        Table+=[[i,count]]
        
    num = Table[0][0]
    count = Table[0][1]
    for i in Table:
        if i[1] > count:
            count= i[1]
            num = i[0]
    return str(num)
def test_int(test_function: str, expected: str, actual: str) -> str:  
    print("Testing function", test_function) 
    if actual == expected:
        print("Test passed -","Expected Result:", expected, "Actual Result:", actual)
        return 1   
    else:
        print("Test Failed -","Expected Result:", expected, "Actual Result:", actual)
        return 0

b = 0
b+=test_list("max_occurrences", "4" , max_occurrences([4,66,4,7, 8,9, 0,2,4,7,]))
b+=test_list("max_occurrences", "66" , max_occurrences([4,66,4,66, 8,66, 0,2]))
b+=test_list("max_occurrences", "7" , max_occurrences([7,66,4,7, 8,9, 7,2,4,7,]))
b+=test_list("max_occurrences", "0" , max_occurrences([4,0,4,7, 0,9, 0,2,0,7,]))

print("The total number passed is", b)

print("\n")


#Exercise 4

def bank_statement(account_balance: float, transaction_history : list) -> float:
    """
     The function takes two input parameters, namely the account_balance a float type 
     number  and transaction_history which is a list of money debited and credited. It returns a 
    float value representing the new account balance in 2 decimal place. 
    
    >>> d+= test_list("bank_statement", "68.12" , bank_statement(60, [27, -80.11, 67.234, -6]))
    Testing function bank_statement
    Test passed - Expected Result: 68.12 Actual Result: 68.12

    >>> d+= test_list("bank_statement", "203.68" , bank_statement(12.556, [12,9, -9.3, 89.3, 90.12]))
    Testing function bank_statement
    Test Passed - Expected Result: 68.12 Actual Result: 203.68

    
    >>> d+= test_list("bank_statement", "-74.84" , bank_statement(76.3, [2.7, -80.11, -67.234, -6.5]))
    Testing function bank_statement
    Test Passed - Expected Result: -74.84 Actual Result: -74.84

    >>> d+= test_list("bank_statement", "199.78" , bank_statement(18.36, [12,9, -19.0, 89.3, 90.12]))
    Testing function bank_statement
    Test Passed - Expected Result: 68.12 Actual Result: 199.78
   """
    x = transaction_history
    i = 0
    new_balance = account_balance
    while i <= len(transaction_history) - 1:
        bit = transaction_history[i]
        new_balance += transaction_history[i]
        i += 1
    return str(round(new_balance, 2))
def test_float(test_function: str, expected: str, actual: str) -> float:  
    print("Testing function", test_function) 
    if actual == expected:
        print("Test passed -","Expected Result:", expected, "Actual Result:", actual)
        return 1   
    else:
        print("Test Failed -","Expected Result:", expected, "Actual Result:", actual)
        return 0

d = 0
d+= test_list("bank_statement", "68.12" , bank_statement(60, [27, -80.11, 67.234, -6]))
d+= test_list("bank_statement", "203.68" , bank_statement(12.556, [12,9, -9.3, 89.3, 90.12]))
d+= test_list("bank_statement", "-74.84" , bank_statement(76.3, [2.7, -80.11, -67.234, -6.5]))
d+= test_list("bank_statement", "199.78" , bank_statement(18.36, [12,9, -19.0, 89.3, 90.12]))
print("The total number passed is", d)

print("\n")

#Exercise 5     
def prime_numbers(lower : int, upper: int) -> list:
    """Function takes two parameters; upper and lower. Returns a list containing 
    all the prime numbers in the range between the lower and upper numbers.
    
    >>> e+= test_int("prime_numbers", "[7, 11]" , prime_numbers(6, 13))
    Testing function prime_numbers
    Test passed - Expected Result: [7, 11] Actual Result: [7, 11]
    
    >>> e+= test_int("prime_numbers", "[1, 2, 3, 5]" , prime_numbers(1, 7)) 
    Testing function prime_numbers
    Test passed - Expected Result: [1, 2, 3, 5] Actual Result: [1, 2, 3, 5]

    >>> e+= test_int("prime_numbers", "[5, 7]" , prime_numbers(4, 9)) 
    Testing function prime_numbers
    Test passed - Expected Result: [5, 7] Actual Result: [5, 7]

    >>> e+= test_int("prime_numbers", "[7, 11]" , prime_numbers(13, 7)) 
    Testing function prime_numbers
    Test passed - Expected Result: [7, 11] Actual Result: [7, 11]

    """
    a = lower 
    b = upper
    f=[]
    if a < b :
        x = range(a , b)
    else: 
        x = range(b, a)
    i = 0 
    for i in x:
        n = 0
        for j in range(2, i):
            if i % j == 0:
                n = 1
        if n == 0 :
            f+=[i]
    return str(f)
                
def test_int(test_function: str, expected: str, actual: str) -> float:  
    print("Testing function", test_function) 
    if actual == expected:
        print("Test passed -","Expected Result:", expected, "Actual Result:", actual)
        return 1   
    else:
        print("Test Failed -","Expected Result:", expected, "Actual Result:", actual)
        return 0                
       
   
e = 0
e+= test_int("prime_numbers", "[7, 11]" , prime_numbers(6, 13)) 
e+= test_int("prime_numbers", "[1, 2, 3, 5]" , prime_numbers(1, 7)) 
e+= test_int("prime_numbers", "[5, 7]" , prime_numbers(4, 9)) 
e+= test_int("prime_numbers", "[7, 11]" , prime_numbers(13, 7)) 

print("The total number passed is", e)


#Main Script
#Exercise 1
print(test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5]" , Fibonacci_sequence(6)))
print(test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5, 8]" , Fibonacci_sequence(7)))
print(test_list("Fibonacci_sequence", "[0, 1, 1, 2, 3, 5, 8, 13]" , Fibonacci_sequence(8)))
print(test_list("Fibonacci_sequence", "[0, 1, 1, 2]" , Fibonacci_sequence(4)))

#Exercise 3
print(test_list("max_occurrences", "4" , max_occurrences([4,66,4,7, 8,9, 0,2,4,7,])))
print(test_list("max_occurrences", "66" , max_occurrences([4,66,4,66, 8,66, 0,2])))
print(test_list("max_occurrences", "7" , max_occurrences([7,66,4,7, 8,9, 7,2,4,7,])))
print(test_list("max_occurrences", "0" , max_occurrences([4,0,4,7, 0,9, 0,2,0,7,])))

#Exercise 4
print(test_list("bank_statement", "68.12" , bank_statement(60, [27, -80.11, 67.234, -6])))
print(test_list("bank_statement", "203.68" , bank_statement(12.556, [12,9, -9.3, 89.3, 90.12])))
print(test_list("bank_statement", "-74.84" , bank_statement(76.3, [2.7, -80.11, -67.234, -6.5])))
print(test_list("bank_statement", "199.78" , bank_statement(18.36, [12,9, -19.0, 89.3, 90.12])))

#Exercise 5
print(test_int("prime_numbers", "[7, 11]" , prime_numbers(6, 13))) 
print(test_int("prime_numbers", "[1, 2, 3, 5]" , prime_numbers(1, 7))) 
print(test_int("prime_numbers", "[5, 7]" , prime_numbers(4, 9))) 
print(test_int("prime_numbers", "[7, 11]" , prime_numbers(13, 7))) 