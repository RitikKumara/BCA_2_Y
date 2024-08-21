

# # a=int(input("enter vlue of a"))
# # b=int(input("enter vlue of b"))
# # c=int(input("enter vlue of c"))
# # D=b^2-4*a*c
# # if (D>0):
# #     x1=(-b+D**0.5)/2*a
# #     x2=(-b-D**0.5)/2*a
# #     print("x1,x2")
# # elif (D==0):
# #     x1=x2=-b/2*a
# #     print("x1,x2")
# # else:
# #     print("imagenry")

# print("Enter marks where max marks is 100 as per subject")
# sub1 = int(input("Enter marks : "))
# sub2 = int(input("Enter marks : "))
# sub3 = int(input("Enter marks : "))
# totalmarks  = sub1+sub2+sub3
# print( "total marks is",totalmarks)
# a =totalmarks /3

# per=(totalmarks/300)*100
# print("per is" ,per)
# if a > 80:
#     print("Grade is A")

# elif a >= 70 and a<80:
#     print("Grade is B")

# elif a >= 60 and a<70:
#     print("Grade is c ")

# elif a>= 40 and a<60:
#     print("Grade is D")

# else:
#     print("Grade is E")
    




#radius = float(input('Enter radius of circle'))
#area = 3.143*(radius**2)
#print(area)


# swap two num using bitwise oprator
# x=int(input("enter a num"))
# y=int(input("enter a num"))
# x=x^y
# y=x^y
# x=x^y
# # # print(x,y)

# n=int(input("enter a num"))
# n=0
# t=n
# d=0
# sum=0
# while(t>0):
#     d=n//10
#     d=d+1
# while(t>0):
#     digit=t%10
#     sum=sum+digit**d
#     t=t//10
# if(n==sum):
#     print("number is armstrong")
# else:
#     print("number is not armstrong")


# n=int(input("enter a num"))
# sum=0
# while(n>0):
#     r=n%10
#     n=n//10
#     sum=sum+r
# print("sum of digit", sum)

# n=int(input("enter a num"))
# rev=0
# t=n
# while(n>0):
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if(t==rev):
#     print("pallidrom")
# else:
#     print("not pallidrom")

# n=int(input("enter a num"))
# fact = 1
# i = 1
# while i<=n:
#      fact = fact*i
#      i +=1
# print(fact)

# n=int(input("enter a num"))
# n=0
# t=n
# d=0
# sum=0
# n=t
# while(t>0):
#     d=n//10
#     d=d+1
# while(t>0):
#     digit=t%10
#     sum=sum+digit**d
#     t=t//10
# if(n==sum):
#     print("number is armstrong")
# else:
#     print("number is not armstrong")



# n=int(input("enter a num"))
# fact=1
# while n>0:
#     fact*=n
#     n=n-1
# print(fact)

a = open('r.txt','r')
b= a.read()

lines = b.count('\n') +1
spaces = b.count(' ')

vowle = 'AEIOUaeiou'
vowles = sum(1 for i in b if i in vowle )
print (f'lines:{lines}, spaces:{spaces}, vowles:{vowles}')