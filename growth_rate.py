def average(scores: list) -> float:
    return (scores[0] + scores[1] + scores[2] + scores[3] + scores[4]) / len(scores)

print(average([10, 40, 58, 63, 75]))
print(average([10, 70, 38, 63, 75]))










##Exercise 5
def polynomial_solution(n: int , solution: list)-> list:
    answers = []
    i = 0
    while i <= len(solution) - 1:
        x = int(solution[i])    
        sum = ( n + (4 * x**2)+ (9 * x**5))
        i+=1
        answers+=[sum]
    return answers
        
        
print(polynomial_solution(4, [2, 5, 2, 3]))

#revision 1
def loop_function(names :list, length: int) -> list :
    x = False 
    y = True
    bool_list = []
    i = 0
    while i <= len(names) - 1:
        if len(names[i]) != length:
            answer = x
            i +=1
            bool_list+=[answer]            
        else :
            answer = y
            i +=1
            bool_list+=[answer]
    return bool_list
        
                               
print(loop_function(["mauu", "cat", "tag", "fil", "nanan"], 3))
        

#revision 2           
def pig_growth(pig_1:int, pig_2:int, growth_rate:int, estimate_rate:int) -> list:
    i = 0
    a = growth_rate/100
    b = estimate_rate/100
    total_weight = pig_1 + pig_2
    final_weight = (pig_1 + pig_2) + (pig_1 + pig_2) * b

    while total_weight < final_weight:
        total_weight += total_weight * a
        i += 1
    
    return [i, total_weight]
        
print(pig_growth(5, 3.4, 2, 0.35))
print(pig_growth(10, 9, 2.8, 33.3))
        

m = int(input("Please enter a number:\n"))
s = 0
for i in range (1, m +1, 1):
    
    s += i
print("sum is", s)

#Exercise 4
def sum_uniques(a:int, b:int, c:int) -> int:
    if a == b and b==c and c==a:
        return 0
    elif a == b and b !=c and c!=a:
        return c
    elif a != b and b!=c and c!= a:
        return a + b + c
    elif a !=c and b==c :
        return a
    elif a == c and b!= c:
        return b
    
print(sum_uniques(3, 4, 5))
print(sum_uniques(3, 3, 5))
print(sum_uniques(5, 4, 5))
print(sum_uniques(15, 5, 5))
print(sum_uniques(3, 3, 3))
    


#Exercise 5
def same_first_last(numbers: list, test:int) -> bool:

    if len(numbers) != 0 and numbers[0] == test and numbers[len(numbers) - 1] == test:
        return True
    else:
        return False
    
print(same_first_last([1, 4, 7, 8], 4))
print(same_first_last([1, 4, 7, 8], 4))
print(same_first_last([4, 4, 7, 4], 4))
print(same_first_last([], 4))
    
 #Exercise 7   
def rotate_right(numbers: list) -> list:
    new_list = [1,1,1]
    new_list[2] = numbers[1]
    new_list[1] = numbers[0]
    new_list[0] = numbers[2]
    return new_list

print(rotate_right([3, 2, 1]))
print(rotate_right([3, 1, 2]))
print(rotate_right([1, 2, 3]))

#Exercise 8
def average2(numbers:list) -> float:
    if len(numbers) > 1:
        return (numbers[0] + numbers[1]) /2
    elif len(numbers) == 1:
        return numbers[0]
    elif len(numbers) < 1:
        return 0
print(average2([2,4,3,4,2]))
print(average2([2]))
print(average2([])) 

#Exercise 9
def first_last(numbers:list) -> list:
    
    t = [numbers[0] , numbers[len(numbers) - 1]]
    return t
print(first_last([2,4,3,4,2]))

#Exercise 10
def count_even(numbers:list) ->  list :
    t = []
    for item in range(0, len(numbers)):
        if numbers[item] % 2 == 0:
            t+=[numbers[item]]
    return t

print(count_even([1,2,3,4,5,6,7,8]))  
print(count_even([11,12,13,14,15,16,17,18])) 

#Exercise 10
def unique_list(alist: list) -> list:
    result = []
    for i in range(len(alist)):
        if alist[i] not in result:
            result += [alist[i]]
    return result 
        
print(unique_list (['cat', 'dog', 'cat', 'bug', 'dog', 'ant', 'dog', 'bug']))  

#Exercise 11


def sum_range2(numbers1: list, m1: int, n1: int) -> int:
    sum2 = 0
    i = 0
    while i < len(numbers1) -1:
        sum2 = numbers1[i]
        i+=1
        Total+=sum2
        
    return sum2
                                        
print(sum_range2([1,2,3,4,5,6,7,8], 1, 6))

