# num = 1025 
# num2 =str(num)
# for i in num2(num2) :
#     print (i)     




# -------- while loop -----> jab condition true ho 
# we have to make while condition false at some point otherwise it will become infinite loop 
# i=0 
# while i < 11 :    # jab tak condition true hai , while  will keep executing 
#     print(i)
#     if i == 5:
#         break
#     i=i+1     




#  num=1054  print usin while loop 

# num=1054 
# while num >0 :
#     print(num%10) # last digit ko print kar dega 
#     num=num //10   # last digit ko permanent remove kardega 





# num=1054
# sum=0 
# while num >0 :
#     last=num%10
#     num=num//10
#     sum = sum+last
# print("sum is : " , sum)  


# check a number is palindrome or not 
# agra mena divison operator use kiya to number  point                                                                     
# num=int(input("enter yourr number "))
# copy=num
# reverse=0
# while num >0:
#     last=num%10 
#     reverse=reverse*10+last
#     num=num//10
# if copy ==reverse :
#     print(f"{copy} is a palindrome number ")
# else:
#     print(f"{copy}is not a palindrome number ")
#   



# --------- string methods -------
# str=input("enter your name ")
# print(str[::-1])

# arrange string 
# name="PyHtoN"
# upper=""
# lower=""
# for i in name:
#     if i.islower():
#         lower=lower+i 
#     else:
#         upper=upper+i
# print(lower+upper)


#  number is armstrong or not 
# armstrong num bo hote hai jitni digit ka number hai utni power lagar kr plus karna aur uska sum us number ke barabar aye 
# num=int(input("enter your number"))
# power=len(str(num))
# sum=0
# copy=num
# while num>0:
#     last=num%10
#     sum=sum+last**power
#     num=num//10
# if copy==sum:
#     print(f"{copy}number is armstrong ")
# else:
#     print(f"{copy} number is not a armstrong ")


# # perfect number 
# num=6
# sum=0
# for i in range (1,num):
#     if num/i ==0:
#         sum=sum+i
# if sum == num :
#     print(f"{num} is a perfect number ")
# else:
#     print(f"{num} is not a perfect ")






#    star pattern printing 
# n=int(input("enter your number "))
# for i in range (1,n+1):
#     print("*"*i)





# ---------> pratice question of function and return <------------
def greet():
    


