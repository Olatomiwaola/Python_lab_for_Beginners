"""
ECOR 1041 Lab 9

Author and Student Number: Olatomiwa Oladunjoye 101210403
"""

#Exercise 1
def first_last(check:list, x:int ) -> bool:
    """
    The function takes two parameters, the first one is a list and the second 
    an int. It then compares the first element and the last element in the list 
    to return a bool if they are equal.
    
    """
    if x == check[0]:
        return True
    elif x == check[-1]:
        return True
    else:
        return False
    
print(first_last([1, 6, 7, 9, 0], 2))
print(first_last([2, 6, 7, 9, 0], 2))
print(first_last([7, 6, 7, 9, 7], 7))
print(first_last([9, 4, 7, 4,  3, 9], 4))
print(first_last([71, 84, 8, 8, 5], 8))


print("\n" * 2)

#Exercise 2
def common_end(team_1: list, team_2: list) -> bool:
    """ 
    The function takes two parameters that are of list type. It then comapres the 
    values of the element in their first and last last index.
    It returns a bool depending if the values are the same or not. 
    
    
    >>>print(common_end([1, 3, 4, 5, 6] , [ 1, 3, 5, 7]))
    True
    
    >>>print(common_end([1, 3, 4, 5, 6] , [ 13, 3, 5, 1]))
    True
    
    >>>print(common_end([44, 3, 4, 5, 6] , [ 1, 3, 5, 6]))
    True

    >>>print(common_end([66, 3, 4, 5, 6] , [ 1, 3, 5, 7]))
    False

    >>>print(common_end([1, 3, 4, 5, 6] , [ 15, 3, 5, 7]))
    False
    
    
    
    
    """
    
    if team_1[0] == team_2[0]:
        return True
    elif team_1[0] == team_2[len(team_2) - 1]:
        return True
    elif team_2[0] == team_1[len(team_1) - 1]:
        return True
    elif team_1[len(team_1) - 1] == team_2[len(team_2) - 1]:
        return True    
    else:
        return False
    

print(common_end([1, 3, 4, 5, 6] , [ 1, 3, 5, 7]))
print(common_end([1, 3, 4, 5, 6] , [ 13, 3, 5, 1]))
print(common_end([44, 3, 4, 5, 6] , [ 1, 3, 5, 6]))
print(common_end([66, 3, 4, 5, 6] , [ 1, 3, 5, 7]))
print(common_end([1, 3, 4, 5, 6] , [ 15, 3, 5, 7]))


print("\n" * 2)


#Exercise 3 

def average(scores: list) -> float:
    """
    Returns the average of all the elements in the list. The function takes a 
    list containing five integers
    
    >>>print(average([1, 4, 5, 6, 7]))
    4.6
    
    >>>print(average([10, 40, 58, 63, 75]))
    49.2

    >>>print(average([1, 42, 15, 76, 97]))
    46.2

    >>>print(average([11, 4, 35, 6, 77]))
    26.6

    >>>print(average([21, 4, 56, 60, 7]))
    29.6
    """
   
    return (scores[0] + scores[1] + scores[2] + scores[3] + scores[4]) / len(scores)
    
print(average([1, 4, 5, 6, 7]))
print(average([10, 40, 58, 63, 75]))
print(average([1, 42, 15, 76, 97]))
print(average([11, 4, 35, 6, 77]))
print(average([21, 4, 56, 60, 7]))

print("\n" * 2)

#Exercise 4 
def reverse(temp: list) -> list:
    """
    Returns a new list containing the same elements in reverse order.
    
    >>>print(reverse([1, 3, 4, 5, 6]))
    [6, 5, 4, 3, 1]
    
    >>>print(reverse([2, 3, 4, 15, 9]))
    [9, 15, 4, 3, 2]
    
    >>>print(reverse([91, 3, 24, 25, 60]))
    [60, 25, 24, 3, 91]
    
    >>>print(reverse([122, 31, 4, 53, 76]))
    [76, 53, 4, 31, 122]

    >>>print(reverse([190, 3, 14, 95, 86]))
    [86, 95, 14, 3, 190]
    """
    li = [1, 1, 1, 1, 1]
    
    li[0] = temp[4]
    li[1] = temp[3]
    li[2] = temp[2]
    li[3] = temp[1]
    li[4] = temp[0]
    return li

print(reverse([1, 3, 4, 5, 6]))
print(reverse([2, 3, 4, 15, 9]))
print(reverse([91, 3, 24, 25, 60]))
print(reverse([122, 31, 4, 53, 76]))
print(reverse([190, 3, 14, 95, 86]))


#Exercise 5

def max_list(list_A: list)-> list:
    """The function takes one parameter which is a list containing three elements 
        in int type. It checks for the maximum and returns a list of the same 
        index with a repetitive of the max number.
        
    >>>max_list ([11, 64, 70])
    [70, 70, 70]

    >>>max_list([54, 64, 709])
    [110, 110, 110]

    >>>max_list([10, 7, 310])
    [310, 310, 310]
    """
    max_list = max(list_A)
    return [max_list, max_list, max_list]

print(max_list([11, 64, 70]))
print(max_list([10,7,110]))
print(max_list([10, 7, 310]))


#Exercise 6
def middle_way(mark_A: list, mark_B: list) -> list:
    """Returns a new list containing the middle elements.
     >>>(middle_way([1, 2, 3], [3,5,8]))
     [2, 5]

     >>>middle_way([6, 10, 2], [6, 10, 2])
     [10, 10]

     >>>middle_way([9, 21, 38], [9, 121, 38])
    [21, 121]

     >>>(middle_way([5, 0, 7], [5, 10, 7]))
     [0, 10]
        """
    li = [mark_A[1], mark_B[1]]
    return li
print(middle_way([1, 2, 3], [3,5,8]))
print(middle_way([6, 10, 2], [6, 10, 2]))
print(middle_way([9, 21, 38], [9, 121, 38]))
print(middle_way([5, 0, 7], [5, 10, 7]))



# exercise 7
def has_elements(lst: list, x: int, y: int) -> bool:
    """ returns True if the list contains x or y or both values

    >>>has_elements ([22, 84,49,11], 11, 22)
    True
    >>>has_elements ([8,10, 6, 4], 5, 11)
    False
    >>>has_elements ([101, 119, 13, 21], 2, 0)
    False
    """

    if x in lst or y in lst:
        return True
    else:
        return False
    
print(has_elements ([22, 84,49,11], 11, 22))
print(has_elements ([8,10, 6, 4], 5, 11))
print(has_elements ([101, 119, 13, 21], 2, 0))



