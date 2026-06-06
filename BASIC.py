# is use for commnet and is also use for """sdgfg"""   
"""variaable 
 don't  




snake case = all samll like sheriyansschool  
pascal case = SherianysSchool
camel case = sheriynsSchool 

data types 
  1 numbers =  integers , float , complex 
complex is the excepption in python 
   


   2 strings = "hello "
                "123"

3 char = a, b,c 


4 bollean   = true or false        
 

                          strings  

c indexing is also  count space 



"""    

# a="sheriyansh " 
# print(a[2:6:1 ])
# """   sclicnig in  a [staring :   stops : steps ]"""

# print(a[6:8])
    


#     #  type casting 
# intger  int()
# float  float()
# boolean bool()
# string   str()
  
# #   input function 
# a=input     

# #  operators 
# arthimactic  + ,-,*,/,% ,**,// 
# assinment 
# logical 
# coparison 
# short hand     a=45
#                a=a+1    

# conditional statement 
# if 
# if else 
# if elif 
# a = int(input("enter number "))
# if a%2==0:
#         print( "number is even  ")
# else:
#         print("number is odd  ")      

#   loops    

# for i in range(10):
#    print("sorry")
# # while  me condition pata  ho 
# # for me usse no. of iteration pata hote hai 

# for i in range(1,11):
#       print(i)

# while(n)
   
# a=input("enter your gender ")
# if a=="male":
#     print("good merning sir")

# elif a=="transgender":
#     print("hello ")
# else :
#     print("good morning mam ")  

# a= int(input("enter you number "))
# for i in range (a):
#     print("hello")
# class 25/05/2026
# #  count a even and odd number within in a range . 
# for i in range (1,51):
#     if i%2==0 :
#         print("even")
#     else: 
#         print ("odd")

#  for count even number and odd number 
# even = 0 # even ka count nhi pata 
# odd = 0 # odd ka count nhi pata 
# for i in range (1,51):
#     if i%2==0:
#         even +=1 # shorthand operator 
#     else :
#         odd +=1# shorthand operator 
# print(even)
# print(odd) 



#  -------- count vowels in string --------   
# s="hello sherry "
# count =0 
# for i in s :
#     if i in "aeiouAEIOU":
#         count +=1 
# print(f"count of vowels are :{count}")





# ---------    you have a range from 1 to 20  you just have to print numbers that  are only divisible by 3 and 5 ------
# for i in range (1,21):
#     if i%3==0  and i%5==0 :
#         print(i)     



# -----------itterative   problems ----------  
#  factoril number   local variable bo hote hai jo kisi function ya loop ke andar hote hai global variable bo hote hai jo ki iteration ke andar nh hote hai 
# count=0 
# num = 10 
# for i in range (1,num+1):
#     if num%i==0:
#         count+=1
# if count ==2 :
#     print(f"{num} is a prime number ")
# else:
#     print(f"{num} number is not prime ")

        
# print(count) 
# doubt  


# a=int(input("enter your name "))
# if a%a==0 and a%1==0 :
#     print("number is prime ")
# else :
#     print("number is not defined ") 



#   ------- print sum of  all factors of a number -----
# sum=0
# num=int(input("enter your number "))
# for i in range (1,num+1):
#     if num%i==0:
#         sum+=i
# print(sum)


# #e. pr quint prime numbers from 1 to 50   h.w. 
# for num in range (1,51):
#     count=0
#     for i in range (1,num+1):
#         if num%i==0:
#             count +=1
#     if count ==2:
#         print(f"{num}is a prime number")    



# ---------->  function   in python  ---------->   
# function ek code ko store kar leta ha fir hhum jab call karte hi to bo value print kar deta hai 
#  day-1 
# def greet():
#     name=input("enter your name  ")
#     print(f"hello{greet}")
# greet()


# return statement 
# return processed code ko function ko dedeta hai 
# def add():
#     a=10
#     b=20
#     return a+b
# print(add())


# def greet():
#     return "hello"


# def add():
#     a=int(input("enter first number "))
#     b=int(input("enter second number "))
#     print(greet())
    
#     c=a+b
#     return c 
# print(add())

# def add (a,b):
#     print(a+b)
# add(10)

# def show (name="rahul",age):
#     print(name,age )

# -----------------> parameters and arguments <--------------------------
# parametrs 
# def add(is bracket ke nadar parametrs diya jate hai )
# arguments 

# arguments bo hote hai jise hum function ko call karte time use karte hai 

# def add (a,b):  # function define karte waqt arguments
#     print(a+b)
# add(10,20)# function call karte waqt arguments 


#   type hinting  (type hinting  ka matalb kis type ka data lena user ko usski ussse hin dena )
# def add (a:int,b:int):#  ye jo a and b hai bo positional parameter matalb a me a ki value jayegi aur b me b ki value 
    
#     print(a+b)
# add(10.2,20)  


# def add (a,b=0):# default parameter  matalb agar user ne uch diya to bo by default value lelega 
#     print(a+b)
# add(10.2) 



#  accept an  parameter na,med as 'n' and print  factorial  of "n" using function
# def fac(n):  #  using recursion 
#     if n==1:
#         return 1
#     return n*fac(n-1)
# print(fac(5)) 

# def factorial (n:int):
#     fact = 1
#     for i in range (1,n+1):
#         fact*=i #  shorthand operator 
#     return fact
# print(factorial (5))






def factorial ():
    n=int(input("enter the number for factorial "))
    fact=1
    for i in range (1,n+1):
        fact*=i
    return n
print(factorial())


    

 

































# day