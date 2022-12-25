def loop_function(names :list, length: int) -> list :
    x = False 
    y = True
    bool_list = []   
    for i in range(0, len(names)):
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



def sum_range(numbers: list, m: int, n: int) -> int:
    mango = m
    nee = n
    sum = 0
    for i in range (mango, nee +1):
        sum = numbers[i]
    sum+=sum
    return sum
print(sum_range([1,2,3,4,5,6,7,8], 3, 6))


password = input("Please enter your password: ")
count = 0
while (password != 'python') and count < 3:
    print ("Try again")
    password = input ("Please enter your password: ")
    count+=1
    if count ==3:
        print("mission abolished")
print("Failed")


for num in range(6):
    for i in range(num):
        print (i, end=" ") 
    print("")
    
str = "hello" 
for i in range(1,3):
    
    print (str[i] ,end ="")