# # d=int(input("enter days:"))
# # m=d//30
# # D=d%30
# # print("total months:",m)
# # print("total days:",D)

# # a = int (input('Enter first value:'))
# # b = int (input('Enter second value:'))
# # area = a*b 
# # print('Area of rectangle is:',area)

# # # area = int(input('Enter area of squre'))
# # # perameter_of_squre = area**0.5
# # # print('Perameter of squre are ', perameter_of_squre ,perameter_of_squre)

# # # radius = float(input('Enter radius of circle'))
# # # area = 3.143*(radius**2)
# # # print(area)

# # # a = int (input('Enter first number:'))
# # # b = int (input('Enter second number:'))

# # # elif a > b:
# # #     print('a is greater')

# # # else:
# # #     print('b is greater ')

# # # a=int(input("enter 1st value"))
# # # b=int(input("enter 2nd value"))
# # # c=int (input("enter 3rd value"))
# # # s=(a+b+c)/2
# # # A=s*(s-a)*(s-b)*(s-c)**0.5
# # # print(A)

# # # # a=int(input("enter a number"))
# # # # elif a%2==0:
# # # #     print ( a,' is even')
# # # # else:
# # # #     print( a,' is odd')

# # #  a = int(input('Enter value of a: '))
# # #  b = int(input('Enter value of b: '))
# # #  c = int(input('Enter value of c: '))
# # #  d = (b**2)-4*a*c
# # #  x1 = (-b-(d**0.5))/(2*a)
# # #  x2 = (-b+(d**0.5))/(2*a)                      
# # #     print(x1 , x2)

# # # from sketchpy import library as lib
# # # obj = lib.vijay()
# # # obj.draw()

# # # a=int(input("enter 1st number"))
# # # b=int(input("enter 2nd number"))
# # # a = a+b
# # # b= a-b
# # # a=a-b
# # # print(a , b)

# # # num = int(input('enter a num: '))
# # # reversed_num = 0
# # # while num != 0:
# # #     digit = num % 10
# # #     reversed_num = reversed_num * 10 + digit
# # #     num //= 10
# # # print("Reversed Number: " + str(reversed_num))


# # sec = int(input('Enter seconds'))

# # min = sec//60
# # hour = min//60
# # day = hour//24

# # print(min , hour , day)



# # # import datetime, time

# # # secs = int(input('Enter time in seconds: '))

# # # result = datetime.timedelta(seconds = secs)

# # # print("\n", result, "\n")

# # print("Enter marks where max marks is 100 as per subject")
# # sub1 = int(input("Enter marks : "))
# # sub2 = int(input("Enter marks : "))
# # sub3 = int(input("Enter marks : "))


# # total_marks  = sub1+sub2+sub3

# # per = total_marks /3

# # print("Perentage is ", per)

# # if per == 100 :
# #     print("Grade is O")

# # elif per >= 80:
# #     print("Grede is A+")

# # elif per >= 70:
# #     print("Grede is A")

# # elif per >= 60:
# #     print("Grede is B+")

# # elif per >= 50:
# #     print("Grede is B")

# # elif per >= 40:
# #     print("Grede is c+")

# # elif per >= 30:
# #     print("Grede is c")
# # else:
# #     print("Fail")

# # # a = int(input("enter lenth"))
# # # b=int(input("enter bidth"))
# # # area= a*b
# # # perimeter=2(a+b)
# # # print("area:-", area )
# # # print("perimeter", perimeter)


# # # length = int(input('Enter the length of garden : '))
# # # width = int(input('Enter the width of garden : '))

# # # calculate_area = length*width
# # # calculate_parameter = 2*(length+width)

# # # print('The area of garden is ',calculate_area)
# # # print('The parameter of garden is ',calculate_parameter)


# # # book1=int(input("enter book1 number:-"))dsddv 
# # # book2=int(input("enter book2 number:- "))
# # # book1,book2 = book2,book1
# # # print("book1=,book=", book1,book2)

# # p=int(input("enter principal ammount="))
# # r=int(input("enter the rate of interest="))
# # t=int(input("enter the time in year="))
# # si=(p*r*t)/100
# # print(si)


# # num = int(input("Enter a num"))
# # fact = 1
# # while num >=1:
# #     fact = fact*num 
# #     num -=1


# # print(fact)

# # n= 5
# # fact = 1
# # i = 1
# # while i<=n:
# #     fact = fact*i
# #     i +=1

# # print(fact)


# # for i in range(6,-1,-1):
# #     print((7-i)*" "+(2*i+1)*'*')

# # for i in range(6,-1,-1):
# #     print((7-i)*' '+(i+1)*'*')

# # for i in range(6):
# #     print((7-i)*' '+(i+1)*'*')

# # for i in range(4):
# #     for j in range(0,i+1):
# #         print(j+1,end=" ")
# #     print()

# # num=1
# # for i in range(4):
# #     for j in range(0,i+1):
# #         print(num,end=" ")
# #         num+=1
# #     print()


# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print('*',end=" ")
# #         # i+=1
# # #     print()
# # # fibonacii series
# # n=int(input("enter a num"))
# # f=0
# # s=1
# # print(f,s)
# # i=3
# # while(i<n):
# #     next=f+s
# #     print(next)
# #     f=s
# #     s=next
# #     i=i+1

# # for i in range(6):
# #      print((7-i)*''+(i+1)*"*")

# # for i in range(6,-1,-1):
#     # print((7-i)*""+(i+1)*"*")


# from turtle import*
# bgcolor("yellow")
# bgcolor("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()

# import calendar
# year=2023
# month=12
# x=calendar.month(year,month)
# print(x)

import phonenumbers
from  phonenumbers import geocoder
phone_number1=phonenumbers.parse("+919720629304")
print("\nphone numbers location\n")