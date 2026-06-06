#                 `` ----------------->ASSINGMENT QUESTION <-----------------

#  Q1. take a user input and print a string 
# a=input("enter your username")
# print(a) 

# Q2. Take a string input from user and Find length of string ?
# a=input("enter your string  ")
# print(len(a))


# Q3. Write a Python program to take a word from the user and print:
    
#     First character
    
#     Fourth character
    
#     Last character
    
#     INPUT - Computer
    
#     OUTPUT -  First character: C
#     Fourth character: p
#     Last character: 
# answer 
# a=input("enter your string  ")
# print("first character of string ",a[0])
# print("fourth character of string ",a[3])
# print("last character of string ",a[-1])



#Q4. print the first five letter , or from 2 to 7 , last four digit 
#WRITE Your code
# a=input("enter your string ")
# print("print first five characters ",a[0:5])
# print("print characters from  string 2 to 7 ",a[2:7])
# print("print four last  characters from string  ",a[-4:])

# Q5. Write a Python program to take a string from the user and convert it into uppercase.
#WRITE Your code
# str1=input("enter your string in lowercase ")
# print(str1.upper())



# Q6. Write a Python program to take a string from the user and convert it into lowercase.
#WRITE Your code 
# str1=input("enter your string in uppercase ")
# print(str1.lower())

# Q7. Write a Python program to take user name as input and print a welcome message.
#WRITE Your code 
# str1=input("enter your name for welcome message ")
# str2="Welome "
# print(str2+str1)


# Q8. Write a Python program to take a string from the user and reverse it.
#WRITE Your code
# str1=input("write your string for reverse it ") 
# print(str1[::-1])
      


# Q9. Write a Python program to take first name and last name from the user and join them.
#WRITE Your code 
# str1=input("enter your first name ")
# str2=input("enter your last name  ")
# print(str1+ str2)



# #Q10. Write a Python program to check whether a word exists in the string or not.
# #WRITE Your code 
# str1=("python is easy ")
# print(("easy")in str1)


#  number is armstrong or not 
# armstrong num bo hote hai jitni digit ka number hai utni power lagar kr plus karna aur uska sum us number ke barabar aye 
# num=int(input("enter your name "))









# ---------------------------> function assingment question <---------------------
#  Question 1: Create a function that takes two numbers as arguments and returns their sum.
# def add ():
#     a=int(input("enter the first number "))
#     b=int(input("enter the second number "))
#     c=a+b
#     return c
# print("sum of two number is ",add())

#  Question 2: Create a function that returns the square of a given number.
# def square():
#     a=int(input("enter the number for square "))
#     c=a*a
#     return c 
# print("square of the number is",square())



## Question 3: Create a function that checks whether a number is Even or Odd.
# def check ():
#     a=int(input("enter the number "))
#     if a%2==0:
#         print("the number is even ")
#     else:
#         print(" the number is odd ")
# print(check())     


## Question 4: Create a function that returns the greater number between two numbers. -->
# def greater():
#     a=int(input("enter the first number "))
#     b=int(input("enter the second number "))
#     if a>b:
#         print("a is greater than b ",a)
#     else :
#         print("b is greater than a ",b)
# print(greater())     



## Question 5: Create a function that calculates the area of a rectangle.
# def area ():
#     a=int(input("enter the length of rectangle "))
#     b=int(input("enter the breadth of rectangle "))
#     c=a*b 
#     return c  
# print("area of rectangle " , area())



## Question 6: Create a function that accepts a name and returns a greeting message.
# def greet ():
#     a=input("enter your name ")
#     return a
# print("hello",greet())



## Question 7: Create a function that returns the sum of numbers from 1 to N.
# def check(n:int): 
#     sum=0
#     for i in range (1,n+1):
#      sum+=i
#     return sum 
# n=int(input("enter the number for sum "))
# print(check(n))   




#  Question 8: Create a function that counts the number of vowels in a string.
# def vowel(n):
#     count=0
#     for i in n :
#         if i in 'aeiouAEIOU':
#             count += 1
#     return count
# n=input("enter your name ")
# print(vowel(n))



## Question 9: Create a function that returns the factorial of a given number. -->
# def factorial():
#     n=int(input("enter the number "))
#     fact=1
#     for i in range (1,n+1):
#         fact*=i
#     return fact
# print(factorial())




## Question 10: Create a function that checks whether a number is Prime or Not Prime.
# def num ():
    
#     n=int(input("enter the number "))
#     count=0   
#     for i in range (1,n+1):
#         if n%i==0:
#             count+=1 
#     if count==2:
#         print ("number is prime ")
#     else:
#         print ("number is not prime")
# num()





## Question 11: Create a function that returns the largest element from a list.
def largest ():
    lst=int(input("enter the list in which you pc largest"))  
    return max (lst)
print("the largest number in  the list is " ,largest())  
      

