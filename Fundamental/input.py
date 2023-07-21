# inpute and output in python
a=int(input("Enter First number :"))
b=int(input("Enter second number :"))
c=a+b
print("Addition of two number :",c)

a=input("Enter First Number :")
b=input("Enter Secind number :")
a=int(a)
b=int(b)
c=a+b
print("Addition of two number :",c)

#how to read data in single line

# a,b = input( "Enter two number ").split(',')
# print(a,",",b)

a,b = map(int,input("Enter Two Number :").split(','))

c = a + b

print(c)

rollNo=87
name = "sagar"
age=23
str="name is : {0} Roll No is : {1} and age is :{2}"

print(str.format(name,rollNo,age))