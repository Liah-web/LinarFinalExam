
'''1) Variable Data Types 
a) Create a variable called "Date_Of_Birth" and assign it the year you were born (or any random 
year) using the right datatype. Print the value of the variable. 
b) What is the difference between an integer and a floating-point number in Python? Backup your 
explanation with an example for each.'''

Date_Of_Birth=2005
print(Date_Of_Birth)

'''An integer does not have a decimal point while a floating-point number has a decimal point
7 is an integer
7.0 is a floating-point number
'''



'''2) Basic Operations 
a) Write a Python program that adds two numbers together and prints the result. 
b) Write a Python program that takes a number as input and multiplies it by 10. Print the result.
'''
#a)
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
sum=a+b
print(sum)

#b)
a= float(input('Enter a number: '))
multiply=a*10
print(multiply)


'''
5) Functions 
a) Write a Python function that takes three numbers as input and return their multiplication.
b) Write a Python function that takes a list of numbers as input and returns the average of all the 
numbers in the list

'''

def Multiplication(a, b, c):
    a=int(input("Enter value for a: "))
    b=int(input("Enter value for b: "))
    c=int(input("Enter value for c: "))
    multi=a*b*c
print(Multiplication())



'''4) Lists and Loops 
a) Create a list of numbers from 1 to 10. Print each number in the list using a loop. 
b) Write a Python program that takes a list of numbers as input and returns the sum of all the 
numbers in the list.
c) Create a dictionary ‘colleague_name’ storing all your colleague names. Hint: Use sequence of 
numbers as their key.'''

Numbers=[1, 2, 3, 4, 5,6,7,8,9,10]
for i in Numbers:
    print(i)



colleague_name={
"0":"Aaliyah",
"1" :"Samuel",
"2":"Ella",
"3":"Opeyemi"
}




'''7) Explain the following terms relating to Python programming Language with examples where needed
a) Escape Sequence
b) Keywords
c) Datatypes
d) Dictionary 
e) Module
f) Interpreter

a. Escape Sequence: These are characters used for special effects or action in a string.

b. Keywords: These are reserved word by python developers for specific purpose.

c. Datatypes: Datatypes are categories of data stored in a variable.

d. Dictionary: Dictionary is a type of data that has a key and a value.

e. Module: Module is a collection of related function.

f. Interpreter: It is a language translator that interpret the codes line by line to the computer.

'''

'''
8) Give a brief history of python, who built it, what led to Python and others, state the current version 
of python you are using.

Python was built by Guido Van Rossum. A couple of Guido Van Rossum junior went to him and told him they will like him to supervise their project. 
The project was building a programming language that is as simple as ABC. Guido accepted but they had a misunderstanding in the long run and the
project was unfinished. Guido got home and challenged himself. He said if his juniors could think of making a program language as simple as ABC, he can
do it also. He succeeded in doing it and named the programming language after one of his favorite TV series "PYTHON". ABC is still in existence and it
is the father of PYTHON but PYTHON is greatly used than it all over the world.
'''

'''10) Give a feedback on this Python course, your instructor and this examination.
The Python course is loaded and complete. It contains what needs to be


My instructor is the perfect man to teach this course. He just knows how to explain for one to understand even though some of the topics are new to us.
He takes his time to give relatable examples thereby helping us to understand better and faster. He is calm and patient.

The examination is quite simple.
'''
