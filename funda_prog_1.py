'''Learning a Prog language like Python starts here....:

PDF - pictorial representation of learning
notes - quick understanding or above and beyond understanding
***python module (IDE) - Help you build the end to end program as an application

Interpreter (line by line compiler) vs Compiler (Entire program compiler)
Python is an interpreter language

How a python program runs? using Intepreter
write a code in a filesystem -> python progname.py -> interpreter read line by line -> check syntax/semantics -> convert to byte code (given line)->
load the bytecode to python virtual machine (RAM) (every time the code will be loaded in the memory) -> CPU will read the bytecode line of the program -> execute it (using RAM as a memory area for holding variables/values/dataset/libraries etc.,)

How a scala program runs? using compiler

While compiling:
write a code in a filesystem -> compile entire program once for all spending some time scalac/javac-> scala code loaded the entire bytecode to java virtual machine (RAM) (first time alone) for compiling  -> compiled code produced as an output in the filesystem

While Executing:
While we execute the code, complete bytecode will be loaded into memory -> CPU will read the bytecode of the program -> execute it (using RAM as a memory area for holding variables/values/dataset etc.,)

vi we43scalaobj.scala

object we43prog extends App
{
val totalnumofasp=70;
print("total number of aspirants is " + totalnumofasp)
}

scalac we43scalaobj.scala
scala we43prog

How a python program use interpreter
vi we43pythonclass.py
class we43prog:
    totalnumofasp=70;
    print("Hello team")
    print("total number of aspirants is " + str(totalnumofasp))
python we43pythonclass.py

Basic programming fundamentals -
Variables & Values & its properties, Comment, STD input/output, block/intend of coding
Operators
Applying some builtin functions
Data types (simple/complex)
Conditional structure
Looping Constructs

2. Specific to Python
OOPS - Framework developers (eg. commiters/contributors of apache spark)
Exception Handling
**FBP - Dataengineers (eg. leverage the spark functions writtern by somebody)

What is a Python Programming Language?
Python is an Intend based, Interpreter (not a compiler based prog lang), high-level (not a boiler plate/low level prog lang), general-purpose (Usage of python libraries across other tools/frameworks is easy) programming language.
Scripting prog.
Func based prog.
Object oriented prog.

for i in list(['weblog_UK.json','weblog_US.json']):
    a=len(i)
    print("total records in ",i,a)

b=100
print(b)

Linux is not an intend based program, it is a block based rather:
for i in weblog*
do
  a=`wc -l $i`
  echo "total records in $i is $a"
done

Basic programming fundamentals:
How to start write programming?
CLI - REPL
REPL - Read Evaluate Print Loop
#Read
name=input()
#Evaluate
isinstance(name,str)
#print
if isinstance(a,str):
    print("given input is a string")
else:
    print("given input is not a string")

Fundamentals of Python Programming...

#loop
for i in list([1,2,3]):
  a=input()
  if isinstance(a,str):
    print("given input is a string")
  else:
    print("given input is not a string")

IDE
pycharm.sh &
create a project -> package -> subpackage -> module (funda_prog_1.py)

Notebook - how to use notebooks - cells, markdowns, magical commands..
jupyter notebooks
zeppelin
databricks notebooks
HUE Webgui
'''

print("************** 1. Basics of Python Programing*************")
'''Day1 Learning (theory)'''
print("How to run a python program")
#right click this module tab and run the program or go to run menu and run or click on the play button in the right top
#or type ctrl+shift+f10

#Fundamentals of Python Programming:
####################################
print("A. Python is an indent based programming language")
#Why Python uses indend based programing ->
#1. Managing the program more efficiently
#2. Better Readablility of the code
#3. For creating the hierarchy of programming.
#4. By default 4 spaces we will give for indends, but more/less spaces or tabs also can be used...

#Indendation is needed for (hierarchy of programming), because we are doing block operation (lines of code) with in the for loop
a=10
b=10
if a==b:
    lst=['weblog_UK.json','weblog_US.json']
    for i in list(['weblog_UK.json','weblog_US.json']):
        a=len(i)
        print("total records in ",i,a)
        if i=='weblog_UK.json':
            print(lst[0])
            if True:
                print(lst[0])

    b=100
    print(b)

#Linux is not an intend based program, it is a block based rather:
'''
for i in weblog*
do
  a=`wc -l $i`
  echo "total records in $i is $a"
done
'''

#indendation has to be uniform within the block of code (not across the block of code)
#below prog doesnt work because we are using different number of spaces between lines of code in a given block
'''
for i in list(['weblog_UK.json','weblog_US.json']):
    a=len(i)
   print("total records in ",i,a)
'''

#below prog doesnt work because we are using different keys like spaces for one line and tab for another line
'''
for i in list(['weblog_UK.json','weblog_US.json']):
        a=len(i)
	print("total records in ",i,a)
'''

#optimal number of spaces has to be 4, but any numbers you can give
for i in list(['weblog_UK.json','weblog_US.json']):
 a=len(i)
 print("total records in ",i,a)

#Can I use Tab rather than space? Yes
for i in list(['weblog_UK.json','weblog_US.json']):
 	a=len(i)
 	print("total records in ",i,a)

if ('1'=='1'):
 print("Same value")


print("B. This is a commented line in Python")
#This is Single line comment in python
'''
This is a multiline comment in python
We can have n  number of lines as comments in python
'''

print("C. Playing with Quotes: Python treats single quotes the same as double quotes as like triple quotes, but has some differences")
#Python treats single quotes the same as double quotes and triple quotes.
a='hello'
a='''hello'''
a="hello"
a="""hello"""
##we can use escape sequence also
name='Inceptez Technology\'s Asset'
print(name)
#Double quotes is used for holding single quoted or other special chars
#internally python apply double quotes if we use escape sequence
name="Inceptez Technology's Asset"
print(name)
name="""Inceptez Technology's Asset "laptop", "mouse" """
#Triple double quotes is used for muliline
#below will consider the entire text in a single line, but wanted to type multiple lines
#For handling paragraph/multilines text, we can use 3 single or doublequotes
name="""Inceptez Technology's Asset 
        "laptop", 
        "mouse" """
print(name)

name='''Inceptez Technology's Asset 
        "laptop", 
        "mouse" '''

#Any programming language learning has to be started first learning about variables
print("Let's learn all about VARIABLES")
'''1. Variable Properties - Dynamic Inference, Dynamic Typed, Strongly Typed'''

#Dynamic inference - based on the assigned value to a variable, it will automatically decides/infer/identify/refers the data type dynamically
a=100
print(type(a))
b='Inceptez'
print(type(b))

#Dynamically typed: If a variable is created with a specific data type, can be changed later
a=100
print(type(a))
#below is possible, because python is dynamically typed language (Duck type language)
a='inceptez'
print(type(a))

'''Scala is a statically typed language
var a="irfan"
#below is possible
a="inceptez"
#below is not possible - because of statically type feature
a=100
'''

#Strongly typed: Python allow us to operate between the variables of same datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.
a=100
b="50"
print(a+int(b))
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
'''Day2 Learning '''
#2. naming convention
#A variable can have camel case or init upper or with underscores
companyName="Inceptez"
CompanyName="Inceptez"
company_name="Inceptez"

#A variable name must start with a letter or the underscore character
companyName1="Inceptez"
_company_name="Inceptez"

#A variable name cannot start with a number
#below doesnt work
#1companyName="Inceptez"

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
company_name_1="Inceptez"
#below doesnt work
#company-name:1="Inceptez"
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#Multiple Variables can be assigned in a single line (Multi Assignment)
#all are different...
age,Age,AGE=10,40,50

#3. How to check a given TYPE is of what datatype we expect isinstance(variable,datatype) & type casting str(), int(), float()
age=10
desc="Inceptez is established before the years of "
#What we are learning here is the usage of few functions like isinstance(),str(),type()
#To understand the age is of what type
print(type(age))
#To check wheter the age is of an expected type
print(isinstance(age,int))
#To convert the age to an expected type
print(str(age))
print(int(age))
print(float(age))

#print(desc + age)
#Above code will not workSince Python is strongly typed language, we can't operate between age:int and desc:str , hence we have to type cast age to string
print(desc+str(age))

#What if we first wanted to check whether the given variable is of a specific type and then typecast it accordingly
#age=10
age='ten'
print(isinstance(age,str))
desc="Inceptez is established before the years of "

#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition
if isinstance(age,str):
    print("no type casting is needed, we can dirctly operate")
    print(desc + age)
else:
    print("type casting is needed, we can't dirctly operate")
    print(desc + str(age))

#4. input (assigning value directly/using input function/passing arguments) / output (print/assigning/return)
#assigning value directly (Hardcoding)
sal=10000
bon=1000
#assigning value directly (applying some functionalities/operations/program on some other/same variables)
gross_sal=sal+bon
sal=sal+bon

#Run time input
#below input will collect salary as string (using input function)
sal=input("enter the salary\n")

#Ternary operator to convert the sal from str to int type, because input will return string type
print("salaray received is "+sal)
gross_sal=sal+bon if isinstance(sal,int) else int(sal)+bon
print("gross salary is ",gross_sal)

#below input will collect salary as string and type cast to int
sal=int(input("enter the salary\n"))
gross_sal=sal+bon
print("gross salary is ",gross_sal)
#pass parameters to a variable when we use functions (FBP and OOPS we learn in detail)
def sal_calc(param1,param2):
 sal=param1; bon=param2;
 print("sal is",sal+bon);
print(sal_calc(30000,1000))

print("D. Standard output options of print statements")
sal=10000
bon=1000
gross_sal=sal+bon
#print statement will be used as a std output function, which will use \n in the end by default, no need of using println like scala kind of lang
#semi colon can be used to seperate a statment if we write multiple statements in one line
print(sal); print(int(sal)+bon)
#below print function is taking only 1 argument (but print can take any number of arguments)
message_to_print="salary is "+str(sal)+" bonus is "+str(bon)+" gross sal is "+str(gross_sal)
print("salary is "+str(sal)+" bonus is "+str(bon)+" gross sal is "+str(gross_sal))
#or
print(message_to_print)

#below print function is taking multiple arguments and printing them individually
print("salary is ",sal," bonus is ",bon," gross sal is ",gross_sal,"any more number of args")

#Formatted string Print statements - positional args
#Positional arguments
str1="salary={0} bonus={1} and gross sal={2}"
print(str1.format(sal,bon,gross_sal))
print("salary={0} bonus={1} and gross sal={2}".format(sal,bon,gross_sal))

#keyword/named arguments
str2="salary={sal} bonus={bon} and gross sal={gs}"
print(str2.format(sal=sal,bon=bon,gs=gross_sal))

#Formatted string Print statements other way (3.6x onwards) - named args
print(f"salary={sal} bonus={bon} and gross sal={gross_sal}")

print("E. Variable (modification) Properties - mutable & immutable properties")
#Variables in python is classified as mutable/modifiable and immutable/non modifiable types
#In python other than set, list, dict all other data types in python are immutable (non changable)
#String is immutable
companyName="inceptez technologies"
#below code try to update i with I is not possible because string in immutable
#companyName[0]='I'

#list is mutable?
#below code try to update i with I is not possible because string in immutable
companyNameLst=companyName.split()
print(companyNameLst)
companyNameLst=['inceptez', 'technologies']
print(companyNameLst)
#['inceptez', 'technologies']
companyNameLst[0]='Inceptez'
print(companyNameLst)
#['Inceptez', 'technologies']

print('F. Simple Datatypes, seperately we learn complex/collection types')
#Sequence Types
#string type -
# indexed sequenced collection of characters/literals
# can be assigned with single, double, triple single/double quotes
# Assign variable with value defining the same type as like the value type if you are sure about the type of the value by hardcoding or typecasting
a:int=10
a:str=str(10)
# Assign variable with value without defining the type if we are not sure about the type of the value, through dynamic inference it will take care
a=10
# Assign variable with value defining the type not like the value type will override the variable type as the value type
a:str=10
#below is also possible
a:int='10'
a:int=int('10')

#How can we define a string type by using dynamic inference
company_name="Inceptez Technologies"
#How can we define a string type by statically defining it (however dynamic inference will override)
#below type of the variable will be overrided with int type
company_name2:str=10
company_name2=10
print(type(company_name2))
#since we know we are assigning the value of string type, we can define the variable type as string
company_name:str="Inceptez Technologies"
#since we know the input function returns string type, we can define the variable type as string
company_name:str=input()

#since I am expecting the type of the variable as int, then i am typecasting the input value type as per the variable type
company_years:int=int(input())

#list, tuple - we learn later

#Numeric Types
#int type
sal=10000
type(sal)
isinstance(sal,int)
sal:int=10000
sal:int=int('10000')

#float type
bonus_percent=8.5
bonus_percent:float=8.5
bonus_percent=float(8)
bonus_percent:float=float(8)

#exponential/complex type
a=100000e100
print(a)

#Misc Types
#bool types: used for performing logical and conditional operations
leap_year_flag_2024=False
holiday_ind=True
print(holiday_ind==True)

#None - nothing or unknow values like null in databases
before_after_irfan_starts_session_tot_num_asp:None=None
if before_after_irfan_starts_session_tot_num_asp is None:
 print(f"don't know how many aspirants are going to attend {before_after_irfan_starts_session_tot_num_asp}")
else:
 print(f"total number of aspirants are {before_after_irfan_starts_session_tot_num_asp}")

#bytes - used for converting the values to byte/binary format before transfer across the network or for processing in a secured fashion
salary=bytes(10000)
type(salary)
memoryview(salary)

#application of bytes
encoded_username=input("pls enter the username\n").encode()
existing_username='hduser'.encode()
if encoded_username.decode()==existing_username.decode():
 print("user already exists")
encoded_username=input("pls enter the username\n").encode()

#Complex types - list, tuples, set, dict we learn later

print('G. Operators')
#Python supports operators -> assignment, arithmatic, comparison/relational, logical, unary (least priority), binary (least priority),
# ternary (least priority), bitwise (least priority)
#One program covers almost all these operators
#greatest of 2 numbers after performing some operation on the first number

###########One Reallife usecase program to bring all types of operators in one Program###########
#Swiggy food purchase -> coupon max discount of 100 or 10% which ever is lesser
#assignment (459,460,461,462,465), arithmatic(462,466, 467, 470), comparison/relational(463,466),# logical (464 if i use or), unary - A variable holds value and an operator (least priority) (466), binary (least priority) (462,466,467,470),
# ternary (least priority) - operating on more than one operators (466), bitwise (least priority) (464 if i use |)
amt=1000
max_offer=100
pct=.10
offer_amt=amt*pct
if (max_offer<offer_amt) or (max_offer==offer_amt):
    print("giving offer of ",max_offer)
    addon_offer_amt=-50
    additional_cashback=amt+addon_offer_amt if amt>100 else amt
    print("amount to pay is",additional_cashback-max_offer)
else:
    print("giving offer of ",offer_amt)
    print("amount to pay is",amt-offer_amt)

#Assignment Operators (=,operator=)- used to assign some values to a variable - return the value/reference as a result
var1='value'
var2='value1'+'value2'
var3=10
var4=5
var4=var4+var3
#or
var4+=var3

#we can assign another object to create a reference
#var2=spark
#both spark and var2 are referencing the same address
#spark
#<pyspark.sql.session.SparkSession object at 0x7fcc36892ac8>
#var2
#<pyspark.sql.session.SparkSession object at 0x7fcc36892ac8>

#Arithmatic Operators (+ - * / % ** ^ ...) - will returns operated value as a result
var1=20
var2=5
print(var1*var2)

# Bitwise Operator ^
# 001 is 1
# 010 is 2
# 011 is 3
# 100 is 4
# 101 is 5
# 110 is 6
# 111 is 7
# 1000 is 8 it goes on like this
print("Bitwise arithmetic operator",3^4)
#https://www.w3schools.com/python/trypython.asp?filename=demo_oper_xor
#011+100 = 111=> 7

#Relational operators (==,>,<,>=,<=,!=) - Used for comparing variables and values and returns boolean type as a result
var1=10
var2=10
print(type(var1>=var2))
print(type(var1==var2))
print(var1==var2)

#Logical Operators (and, or, not) - apply logic between multiple output of the relational operators and Returns boolean
#or - returns true if any one of the result is true
print(((var1>var2) or (var1==var2)))
#and - returns true if all of the result is true
print(((var1==var2) and var1==10))
#not - returns false (if all of the result is true in case of and) (if any one of the result is true in case of or)
print(not((var1>var2) or (var1==var2)))

#Bitwise Operators (&, |, ~) - same like logical operator (Costly to use because - internally bitwise will do a comparison bit by bit for producing the true or fase result)
print(((var1>var2) | (var1==var2)))
print(((var1>var2) & (var1==var2)))
print(~((var1>var2) or (var1==var2)))

print("H. String & Num operations using Built in functions")
#how to understand and use builtin functions (Very important part of our whole learning)
#Rather than performing this much lines of code to update the company name, we can simply achieve using a function
company_name="inceptez technologies"
complst=company_name.split()
complst[0]='Inceptez'
complst[1]='Technologies'
company_name=complst[0]+' '+complst[1]
print(company_name)

#Rather than performing this much lines of code to update the company name, we can simply achieve using a function
#To understand a function, try to extend a given function (identified based on the name or if we recall a functionname) and hover to understand the description+signature of the function
#To view the source code or to see the module/class this function is belonging to - press ctrl+mouse click
#Inside the module you again click ctrl+mouse click to understand this particular function is used in what are the modules
company_name="inceptez technologies"
print(company_name.capitalize())
print(company_name.title())
company_name="inceptez technologies {0} {1}"
print(company_name.format("pvt.","ltd."))
company_name="inceptez technologies {arg1} {arg2}"
print(company_name.format(arg2="ltd.",arg1="pvt."))
#We have to recall this function since we use it regularly
#WE ARE NOT GOING TO LEARN HOW TO MEMORIZE OR RECALL ALL THE 1000+ OF FUNCTIONS THAT CORE PYTHON/NUM PY/PYSPARK or any libraries provided
company_name="inceptez technologies pvt ltd"
print(company_name.split(" ",2))

print(company_name.encode('utf-8','ignore'))
print(memoryview(company_name.encode('utf-8','ignore')))

#used to find the index value of the given subset of string searched in a range of index
print(company_name.index('ech',5,20))
print("Prabhu Govindan".replace('a','x',1))

print("Prabhu Govindan".count('a'))
print("Prabhu Govindan".count('a',0,5))
print(" ".isspace())
print("abc".islower())
print("Abc".istitle())
print("Abc1".isalpha())
print("Ab212c".isalnum())
print("Abc".isnumeric())
print(" ab cd ".strip())
print(" abcd ".rstrip())
int1=100
print(int1.__floor__())
flt=100.5
print(flt.__lt__(100.6))

import math
print(math.floor(flt))

##### All about Variables is completed here #######

#####CONTROL STRUCTURE LEARNING STARTS HERE#############
#Controlling of flow of program will be done through control structures - Conditional & Looping Constructs
print('I. Conditional Structure')
#prabhu "if" you have mobile pls call me "else if" you have pager pls text me "else" pls come to my home

#if conditional structure & case conditional structure (python programming uses case conditions is special cases) (exception handling)
#I can/must/minimum have if condition alone - TRUE
#I must have if condition with else statement - FALSE
#I can have only else if or else statement - FALSE (every conditional struct should starts with if)
#I can have if condition with else condition alone - TRUE
#I can have if condition with else if condition alone - TRUE
#I must have if condition with else if condition and else statement also - FALSE
#I should have my conditional structure started with if (if should be used only once), but can have multiple elif and should have only one else

#what is a conditional structure?
#CS help us evaluate some condition and help us make decision accordingly to control the flow of program
#when do we use conditional struct?
#If we have options

#wanted to travel from chennai to mumbai?
#conditional structures we can use if, elif, else
abroad_flight=300000
amount_in_hand=350000
if amount_in_hand>=abroad_flight:
    print("Travelling to Sweden, as I have money")
    print("enjoy my holidays")

road=800
train=800
if road<=train:
    print("choosing road transport, since train is costly")
else:
    print("choosing train transport, since train is more convenient or road is more costly")

road=900
train=900
flight=1700
if road<=train and road<=flight:
    print("choosing road transport")
elif train<=road and train<=flight:
    print("choosing train transport")
elif train==road and train==flight:
    print("choosing flight transport")
else:
    print("choosing flight transport")

#This is a nested conditional structure, which has to be used appropriately, needs lot of iterative testing
road=1600
train=1400
flight=1500
if road<=train:
    if road<=flight:
        print("choosing road transport")
    else:
        print("choosing flight transport")
elif train<=road:
    if train<=flight:
        print("choosing train transport")
    else:
        print("choosing flight transport")
else:
    print("choosing flight transport")

#Find the greatest of 3 numbers using built in functions (max(list of values))
a=10
b=10
c=30
#Santhosh's code
lst=[a,b,c]
max_lst=max(lst)
print(max_lst)

dict1={"a":10,"b":10,"c":30}
max_lst=max(list(dict1.values()))
print(max_lst)

#Find the greatest of 3 numbers or find whether all the numbers are same
a=10
b=20
c=20
#Anirudh - if 2 variables are same, this code will not handle that
if a>b and a>c :
  print("a is the greatest")
elif b>a and b>c:
  print("b is the greatest")
elif c>a and c>b:
  print("c is the greatest")
else:
  print("all are same")

#Ashutosh Code - not covering all are same
n1=input("enter first number")
n2=input("enter second number")
n3=input("enter third number")
if (n1>=n2) & (n1>=n3):
    print("n1 is highest number")
elif (n2>=n1) & (n2>=n3):
    print("n2 is highest number")
else:
    print("n3 is highest number")

#Akshay's code
if a==b and a==c :
    print("All are same ")
elif a>=b and a>=c :
    print(a, " is the greatest ")
elif b>=a and b>=c :
    print(b, " is the greatest ")
else :
    print(c, " is the greatest ")

#Ranganayaki's code
a=10
c=10
b=30
if a==b and a==c :
    print("All are same ")
elif a>=b and a>=c :
    print(a, " is the greatest ")
elif b>=a and b>=c :
    print(b, " is the greatest ")
else :
    print(c, " is the greatest ")

#Abdul's code - We can remove z==x condition (since it is covered in the first 2 conditions)
#use >= rather than > alone
x=10
y=10
z=10
if x==y and y==z and z==x:
  print("number is same")
elif x>y and x>z:
  print("greatest number is",x)
elif y>x and y>z:
  print("greatest number is",y)
else:
  print("greatest number is",z)


#Find the greatest of 3 numbers or find whether all the numbers are same using nested conditional structure
a=10
b=10
c=30
#Ranganayaki's code - Will caught behind a condition
if a==b:
    if a==c:
        print("All are same ")
elif a>=b:
    if a>=c:
        print(a, " is the greatest ")
elif b>=a:
    if b>=c:
        print(b, " is the greatest ")
else:
    print(c, " is the greatest ")

#Akshay's Code - We are directly concluding a==b and b!=c (don't conclude directly), changing rest to nested conditional structure
if a==b and b!=c:
    if a>=b and a>=c :
        print(a , " is the greatest ")
    elif b>=a and b>=c :
        print(b," is the greatest ")
    else :
        print(c , " is the greatest ")
else :
    print("All are same ")

#Modified Code:
if a==b and b==c:
    print("All are same ")
elif a>=b :
    if a>=c :
        print(a , "a is the greatest ")
    elif c>=a :
        print(c, "c is the greatest ")
elif b>=a :
    if b>=c :
        print(b , "b is the greatest ")
    elif c>=b :
        print(c, "c is the greatest ")
else :
    print(c , "c is the greatest ")

#Hinthu Priya's code - without all are equal condition
#If we want to add all are equals condition also (conclude that in the starting)
if a==b and a==c:
    print("all are same")
elif(a>b):
    if(a>c):
        print(f"the greatest number is ,{a}")
    elif(b>c):
        print("the greatest number is ,b")
    else:
        print("the greatest number is ,c")
elif(b>c):
        print("the greatest number is ,b")
else:
        print(f"the greatest number is ,{c}")


#Before we write some complex/nested conditional structure, we have first create a psedo code
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or cloud or devops else inform course is not available
# "if" user choosen ask anything ->

popup="clicked"
if popup=="clicked":
    print(f"choose any of the given option")
    opt = input("Choose upcoming batch or ask anything \n")
    if opt=="upcoming batch":
        tech = input("Choose the technology data engg or cloud or devops \n")
        if tech=="data engg":
            print("""Duration : 350 Hours Launch date : 28 February, 2024""")
        elif tech=="cloud":
            print("""Duration : 250 Hours Launch date : 31 March, 2024""")
        elif tech=="devops":
            print("""Duration : 200 Hours Launch date : 31 March, 2024""")
        else:
            #pass is used to skip the given block of code in the conditional structure
            pass
            #print(f"""Sorry we don't the course {tech} you have chosen""")
    elif opt=="ask anything":
        mail_or_phone = input("Choose the mail or phone option \n")
        if mail_or_phone=="mail":
            print(f"""We will send you the details in mail {mail_or_phone}""")
        else:
            print(f"""We will reach you through phone {mail_or_phone}""")
    else:
        print("choose the right option of upcoming batch or ask anything")

#Day 3
print('J. Looping Constructs')
#Looping Construct concepts ->
'''
Category -> 
Conditional looping (entry & exit) eg. while i<=j or while True (do while loop) 
Un Conditional looping - for loop
Types (for, while + do while - not available directly in python (rather we use while True (exit controlled)))
break -> break will terminate the iteration of a loop and come out of the loop 
& continue -> continue will skip the iteration of a loop and continue to the next iteration
'''
#Iteration or repetitive execution of the some tasks across data or programs is called loops
#Two way of Performing Looping - Conditional & UnConditional loopings
#application of bytes
existing_password='hduser'.encode()
#for loop is an unconditional looping
lst=list(range(3))#Itearable values
for i in lst:
    print("100 lines of code")

#A Realtime Example of for loop on a list of salary (Unconditional Looping)
cts_sal_list=[10000,20000,5000,12000]
total_sal=0
for sal in cts_sal_list:
 print(f"salary is {sal}")
 total_sal=total_sal+sal
 print(f"total sal is {total_sal}")

print(f"total sal (final sal outside of the loop) is {total_sal}")


#while loop is an conditional looping
initial=1
maxval=3
while initial<=maxval:
    print("execute 100 lines of code",initial)
    initial=initial+1
print("loop came out",initial)

#Realtime example of a conditional looping
initial=2
maxval=3
storedpass='hduser'
while initial<=maxval:
    enteredpass=input("enter the password\n")
    if enteredpass==storedpass:
        print("login success")
        break
    else:
        initial+=1

#Let's try to understand the looping concept in detail with some case studies including the other constructs like break and continue:
#First lets' learn For loop -
#For loop will run on an iterable type only
#For loop is a unconditional looping
#For loop - number of iterations are already known
str1="irfan"
for i in str1:
    print(i)

#How to write a simple for loop
odd_lst=list(range(1,10,2))
print(odd_lst)
for elem in odd_lst:
    print("elements",elem)

#Nested For loop
#I wanted to calculate bonus applied salary
emp_lst=["Gaya","Anirudh","Praveena","Venkatesh","Srilakshmi"]
sal_lst=[10000,20000,5000,15000,20000]
bonus_percent=10
#for empname,sal in emp_lst,sal_lst:#We can't iterate on more than one list using a single looping construct
#    print(f"bonus applied salary for {empname} is ",int(sal+(sal*(bonus_percent/100))))
#This below approach for finding empname and the salary of the given employee, will not work as we expected
for sal in sal_lst:
    sal_index=sal_lst.index(sal)
    empname=emp_lst[sal_index]
    print(f"bonus applied salary for {empname} is ", int(sal + (sal * (bonus_percent / 100))))

#Let's try with Nested looping: The below nested looping will not work
emp_lst=["Gaya","Anirudh","Praveena","Venkatesh","Srilakshmi"]
sal_lst=[10000,20000,5000,15000,20000]
for empname in emp_lst:
    for sal in sal_lst:
        print(f"bonus applied salary for {empname} is ", int(sal + (sal * (bonus_percent / 100))))

#Let's try with Nested looping: Using an important function called "enumerate" we can get the index also with the element and apply in other list
empid_lst=[1,2,3,4,5]
emp_lst=["Gaya","Anirudh","Praveena","Venkatesh","Srilakshmi"]
#        0:10k,1:20k,2:5k,3:15k,4:20k
sal_lst=[10000,20000,5000,15000,20000]
for idx,sal in enumerate(sal_lst):
        print(f"bonus applied salary for empid {empid_lst[idx]} and empname {emp_lst[idx]} is ", int(sal + (sal * (bonus_percent / 100))))

#When Do we use Nested For loop
#An University wanted to provide the subjects to all affliated colleges
college_lst=["SVN","REC","ABC","XYZ"]
subjects_lst=["ENG","MAT","PHY","CIVIL","MECH"]
college_sections=["A","B","C"]
for colleges in college_lst:
    for secs in college_sections:
        for subjects in subjects_lst:
           print(f"College {colleges} is getting subjects of {subjects} for the sections of {secs}")

#For Loop with Break and Continue constructs/clauses:
#Break is used to break the execution of the loop by come out of the loop if a given condition matches
#Continue is used to skip the given iteration of the loop (and execute the next iteration) if a given condition matches
sal_lst=[10000,20000,5000,15000,20000]
for sal in sal_lst:
    if sal>10000:
        print("Bonus applied salary is ", int(sal + (sal * (bonus_percent / 100))))
    print(f"Loop runs ")

#Let's fine tune the above looping construct to only iterate the required number of times (3 times only rather than 5 times)
#The loop will run only 5+1 times
#Push down optimization
sal_lst=[10000,20000,5000,15000,20000,18000,22000,9000,8000]
sal_lst.sort(reverse=True)
print(sal_lst)
for sal in sal_lst:
    print(f"Loop runs ")
    if sal>10000:
        print("Bonus applied salary is ", int(sal + (sal * (bonus_percent / 100))))
    else:
        break

#Break is only effective if we sort the data?
#exists in sql's
lst_aspirants=["Gaya","Anirudh","Praveena","Sriram","Venkatesh","Srilakshmi","Sriram","Irfan"]
for i in lst_aspirants:
    print("looping")
    if i=='Sriram':
        print("Sriram is present")
        break

#continue construct: continue will help skip the current iteration and continue with the next iteration
lst_states=['TAM','KER','PON','TEL','GOA','KAR']
for states in lst_states:
    if states =='PON' or states=='GOA':
        print("no tax is applicable",states)
        continue#continue will help skip the current iteration and continue with the next iteration
    print("100 lines of subsequent code I am running",states)

#Usecase1: Try create tables for your kids from 2 to how many tables (get as an input)?
# using simple or nested for loop, skip the 5 and 10 tables
#Table has to created upto 12 numbers
'''
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
'''

#Ranganayaki's code
#Usecase1: Multiplication table
start_number = 2
end_number = int(input("Give the end number for table generation:"))
for i in range(start_number, end_number + 1):
    if i == 5 or i == 10:
        continue
    else:
        print(f"Multiplication table for {i}:")
        print("--------------------------")
        for j in range(1, 13):
            result = i * j
            print(f"{i} * {j} = {result}")

        print()  # Print an empty line to separate tables

#Ashutosh's code
#use case 1 #
for i in range(1, 11):
    for n in range(1, 11):
        if i == 5 or i == 10:
            continue
        else:
            tbl = i * n
            print(f"{i} * {n} = {tbl}")

#Hinthuu Priya's code
#multiplication table using nested for loop
a=int(input("enter the starting table"))
b=int(input("enter the ending table"))
b+=1
for i in range(a,b):
    print(f"multiplication table {i}")
    if i==5 or i==10:
        print(f"skip {i} table")
        continue
    for j in range(1,13):
        print(f"{i}*{j}= {i*j}")

#Akshay's code:
number = int(input("Enter the number for table : "))
print("Nested loop :")
# using nested for loop
for i in range (1,number+1,1):
    for j in range (0,11,1):
        if(i==5 or i ==10):
            continue
        else :
            print (f"{i} x {j} = ", i*j )

#While Loop

#Looping constructs available in Common Prog languages - for, while and do while
#Looping constructs available in Python language - for and while (no do while is available in python)
#Types of Looping - Entry Control & Exit Control loops


#While loop will run on a condition only
#While loop is a conditional looping
#Since while loop is conditional, it supports else option also
#While loop - number of iterations is unknown
#While loop has two types of looping like entry controlled (while loop with condition) and exit controlled looping (while loop with no condition (True))
#While loop is used to create infinate loops (hence it has to be used cautiously)
while False:
    print("Do one thing")
else:
    print("Do some thing else")

#How to create infinate loop using while to run some process/operation continuously
#In the other hand if we don't manage the conditions properly, it will leads to infinate looping
#while True:
#    print("Do one thing")
#else:
#    print("Do some thing else")

#Convert the for loop into while loop - conclude which is better to use for iterating list of values? FOR LOOP is considerable
sal_lst=[10000,20000,5000,15000,20000]
for sal in sal_lst:
    if sal>10000:
        print("Bonus applied salary is ", int(sal + (sal * (bonus_percent / 100))))
    print(f"Loop runs ")

sal_lst=[10000,20000,5000,15000,20000]
tot_elem=len(sal_lst)-1
initial_idx=0
while initial_idx<=tot_elem:
    print(f"Loop runs ",initial_idx)
    sal=sal_lst[initial_idx]
    print(sal)
    if sal>10000:
        print("Bonus applied salary is ", int(sal + (sal * (bonus_percent / 100))))
    initial_idx+=1

#Realtime Example of using While loop: Entry controlled loop
#Login username/password used in our routine life
# username=input("User name\n")
# storedpasswd="hduser"
# attempts=1
# maxattempts=3
# while attempts<=maxattempts:#Entry controlled loop - loop will execute only if the condition met (This loop may execute 0 to 3 times)
#     enteredpasswd = input("Enter passwd\n")
#     if storedpasswd==enteredpasswd:
#         print("Login success")
#         break
#     else:
#         print("Enter the right password")
#     attempts+=1
# else:#this else will execute when the while condition become false
#     print("login failed")

#Exit controlled loop - Can you try this program by referring this once
#
username=input("User name\n")
storedusername=["hduser","irfan","anand"]#sudoer file in linux
storedpasswd="hduser"
attempts=1
maxattempts=3
while True:#Exit controlled loop - loop will execute only if the condition met (This loop may execute 0 to 3 times)
    if storedusername.count(username)==1:
        #print("username is there in our system")
        enteredpasswd = input("Enter passwd\n")
        if storedpasswd==enteredpasswd:
            print("Login success")
            break
        elif attempts>=maxattempts:
            print("max attempts reached, exiting out")
            break
        else:
            print("Enter the right password")
            attempts+=1
    else:
        print(f"{username} is not in the sudoers file.  This incident will be reported.")
        break

#Usecase2 related to exit controlled loop (do while loop) + break & continue:
#Create a scheduler program to run a code minimum once or continue to run multiple hours + skipping odd hours
#eg. sfm_insure.py (some print statement)
starthr=0
endhr=4
oddhr=[]
evenhr=[]
hrs=list(range(0,24))
for i in hrs:
 if i%2 != 0:
  print(i)
  oddhr.append(i)
 else:
  evenhr.append(i)

#Hindu Priya's Code
while True:
    print("sfm_insure.py is running")
    for _ in range(starthr,24):#unconditional looping
        starthr=starthr+1
        if (evenhr.count(starthr)):
            print(f"continue the loop for hour {starthr}")
            print("sfm_insure.py is running")
        elif oddhr.count(starthr):
            print(f"skip the loop for the hour {starthr}")
            continue
    else:
        break#Exit control

#Akshay's code
start_time = int(input("Enter the start time in 24 hours format "))
end_time = int(input("Enter the end time in 24 hours format "))

#using for loop
print("Using for loop")
for i in range (start_time , end_time+1 ,1):
    if i%2==0 :
        print("Script is running ")
    else :
        continue;
#using while loop
print("Using do while ")
while start_time <= end_time:#entry control loop
    if start_time%2==0 :
        print("Script is running " , start_time)
        start_time=start_time+1
    else :
        start_time=start_time+1
        continue;

#Anirudh's code
#Usecase2 related to exit controlled loop (do while loop) + break & continue:
#Create a scheduler program to run a code minimum once or continue to run multiple hours + skipping odd hours
#eg. sfm_insure.py (some print statement)
starthr=int(input("Enter the start hr of your choice\n"))
endhr=int(input("Enter the end hr of your choice\n"))
count=0
while True:#Exit control loop
  if(starthr<=endhr):
     if starthr%2==0:
       script_name="sfm_insure.py"
       print(f"Run the script {script_name}")
       count+=1
       starthr+=1
     else:
       starthr+=1
       continue
  else:
    print("Start Hour cant be greater than end hr ,Please change the values")
    break
print("No of times the script has run",count)

#Pseudo code for this?
while True:
    print("sfm_insure.py is running")
    starthr = starthr+1
    if (starthr<endhr):
        print("continue the loop")
        if oddhr.count(starthr):
            print("skip the loop")
            continue
    else:
        break
##############################################Condition Structure & Looping Constructs####################################

#Day 4
print('K. Collection Types')
#Application of using collection types in realtime world?
#Self served metadata driven Data movement automation (DMA) tool
#{"process":"ETL Process1","source":["hive","Bigquery"],"target":["HDFS","GCS"],"cols":["custid","upper(custname) as upper_custname"],"tablename":"customer","where":"(city='chennai')","gcs_uri":"gcs://abc/xyz_bucket/"}
import json
openfile=open("/home/hduser/sparkdata/file2.json",'r')
readjsonfile=json.load(openfile)
cols=readjsonfile['cols']
query='select '+cols[0]+','+cols[1]+' from '+readjsonfile['tablename']+' where '+readjsonfile['where']+';'
sources=readjsonfile["source"]
type(sources)
for i in sources:
 print(f"running the query {query} on the db of {i}")
 print(query)

#Hive -    array,        struct, map
#Python -  list/set,     tuple,  dict

#What is a collection type? Group of elements can be accessed using some way (that holds the list of values in the 3rd dimension).
#A Collection type is a Group/Collection/list of elements/items/values and collections can be organized/accessed using index/key/value

#Examples of Collection Types:
#    i0/p1,i1/p2,i2/p3
#list
lst1=[10000,20000,15000]#list Notation [], accessible using index starts from 0, items of homogeneous types, accessed using index
#Realtime example of list in database/tables - list can be used to store values of the columns

#dictionary
dict1={1:10000,2:20000,3:15000}#Dictionary, Notation {key1:val1,key2:val2,key3:val1}, items of k,v pairs, accessed using key
dict2={"custid":1,"fname":"Arun","age":33}
#Realtime example of dict in database/tables - dictionary can be used to store column along with values as a key and value

#tuple
tup1=(1,"Irfan",10000,"Chennai")#Tuple, Notation (), items of hetrogeneous types, accessed using index
#Realtime example of tupe in database/tables - tuples can be used to store one record

#set
set1={10,5,3,15,17,10,5} #Set, Notation {}, items of homogeneous types of ordered and distinct values, cannot be accessed directly using index/key, only accessible using values
#Realtime example of tupe in database/tables - store the data in a ordered and deduplicated fashion (primary key), to perform set operation union, intersect, minus, adjoint, disjoint...

#Notataions:
#list- []
#dict - {k,v}
#tuple- ()
#set- {}

#Example of all collection types used:
#{'process': 'ETL Process1', 'source': {'hive', 'Bigquery'}, 'target': ['HDFS', 'GCS'], 'cols': ['custid', 'upper(custname) as upper_custname'], 'tablename': 'customer', 'where': "(city='chennai')", 'uris': ('gcs://abc/xyz_bucket/', 100)}

#Different types of collection types? in the order of importance
#list, dict, tuple, set

#Why we need collection types?
#To manage/store/parse the complex dataset in a hirarchical/nested/complex structure stored or to process semi structure data, nested data,
# dynamic schema-ful data (avro), variable data/metadata, for a data or metadata driven approaches..

#Different characteristics of collection types?
#Iterable (looping), mutable (changable) - updatable (modifyable) & resizable (added/removed), accessible (select using index, position, value, key)

######What are the topics we have to learn in collection types#######
#Iterable? Yes, all collection types are iterable in python.
for i in lst1:
    print(i)

dict2={"custid":1,"fname":"Arun","age":33}
for i in dict2:
    print(i)

for i in tup1:
    print(i)

for i in set1:
    print(i)

str1="hello"#string is also iterable, because it is an indexed sequenced collection of characters
for i in str1:
    print(i)

#Notation, access, resizable/mutable/immutable?  insert/update/delete, functions to apply
#All the above we are going to see in detail

print("List type in python (PRIORITY1)")
#Notation:[]
#Accessed using ? index
#Definition: Indexed, sequenced collection of homogeneous elements

print("list operations")
#List can be hetrogeneous too (but not suggested, why ? because while operate between the elements of the list, program fails because python is a strongly typed language)
sal_lst=[10000,20000,'five thousand',30000]
sum_sal=0
#for i in sal_lst:
#    sum_sal=sum_sal+i

#All the python collections are iterable - we have seen already...
sallst=[10000,20000,30000]
for i in sal_lst:
    print(i)

#select/access
second_sal=sallst[1]
print(f"access and print the second salary of the list {second_sal}")

#insert/update/delete (list is mutable, hence updating and resizing (add/removing) is possible)
sallst=[10000,20000,30000]
print("list before appending",sallst)
#append in the last (proves list is mutable/resizable/can be inserted)
sallst.append(25000)#append used to add elements into the existing list in the last
print("list after appending",sallst)

#insert in the index position
sallst=[10000,20000,30000]
sallst.insert(2,25000)#insert used to add elements into the existing list in the given index position
print("list after inserting in an index of 2",sallst)

#update the list elements (mutable)
citylst=['chn','hy','mum','chn','mum']
citylst[1]='hyd'
print("list after updating in an index of 1 value updated from x to y",citylst)

#delete the elements of the list using value
citylst=['chn','hy','mum','chn','mum']
citylst.remove("mum")

#delete multiple same elements using the value
citylst=['chn','hy','mum','chn','mum']
for i in citylst:
 if i=='mum':
  citylst.remove(i)

#pop (delete) the elements of the list using index
citylst=['chn','hy','mum','chn','mum']
citylst.pop(1)

print("list after popping out a given index element",citylst)

#search for a value with in the given index (range) value and pop(remove) it
citylst=['chn','hy','mum','chn','mum']
idx_first_mumbai=citylst.index('mum',0,3)
citylst.pop(idx_first_mumbai)
print("sal_lst after removing out first occurance of the given elements",idx_first_mumbai)

citylst=['chn','hy','mum','chn','mum']
idx_another_mumbai=citylst.index('mum',3)
citylst.pop(idx_another_mumbai)
print("sal_lst after removing out another occurance of the given elements",idx_another_mumbai)

citylst=['chn','hy','mum','chn','mum']
for i in citylst:
 if i=='mum':
     mumbai_idx=citylst.index(i)
     citylst.pop(mumbai_idx)

print("city list after removing out all occurances of the given elements",idx_another_mumbai)

#Wanted to remove the duplicate in a given list?
citylst=['chn','hy','mum','chn','mum','mum']
#Convert to set and back to list
citylst=list(set(citylst))
print("deduplicated city list =",citylst)

#certain builtin functions to try out on list
citylst=['chn','hy','mum','chn','mum']
print("count the occurance of the given value",citylst.count('mum'))
citylst.sort()#ascending
citylst.sort(reverse=True)#descending
print("sorted in asc/desc list is ",citylst)

citylst=['chn','hy','mum','chn','mum']
citylst.reverse()

print("reversed list is ",citylst)

newcitylst=citylst.copy()
print("shallow copy of a list to another list",newcitylst)

citylst=['chn','hy','mum','chn','mum']
citylst2=['del','noi','kol']
citylst.extend(citylst2)
print("extended list with number of elements is ",citylst,len(citylst))

citylst=[]
citylst1=['chn','hy']
citylst2=['mum',]
citylst3=['noi',]
citylst.append(citylst1)
citylst.append(citylst2)
citylst.append(citylst3)
print("appended list with number of elements is ",citylst,len(citylst))

citylst=['chn','hy','mum','chn','mum']
citylst.clear()
print("empting the list",citylst)

print("Dictionaries (mutable) - {k:v, k:v}")
dict1={"custid":1,"fname":"Arun","age":33}

#Access a dictionary - using key
fname=dict1["fname"]
age=dict1["age"]
print("Accessing the value of a key",fname,age)

#Adding Items - if the key is not found
dict1={"custid":1,"fname":"Arun","age":33}
dict1.update({"city":"Chennai"})
print(f"added Dictionary",dict1)

#Updating Items - if the key is found
dict1.update({"age":34})
print(f"updated Dictionary",dict1)

#Removing an Item (from the last)
dict1={"custid":1,"fname":"Arun","age":33}
dict1.popitem()
print(f"Removed item Dictionary",dict1)

#Delete(pop) the given key
dict1={"custid":1,"fname":"Arun","age":33}
dict1.pop("age")
print(f"Popped out Dictionary",dict1)

#Delete all the elements of a dict
#dict1.clear()
print(f"cleared Dictionary",dict1)

#Iteration of Dictionary
#Iterate on the items of the Dict - will return what datatype???tuple
dict1={"custid":1,"fname":"Arun","age":33}
for i in dict1.items():
    print(i)

#Iterate on the keys of the Dict - will return what datatype???respective key's datatype
for i in dict1.keys():
    print(i)

for i in dict1:
    print(i)

#Iterate on the values of the Dict - will return what datatype???respective value's datatype
for i in dict1.values():
    print(i)

#Some additional functions
dict1={"custid":1,"fname":"Arun","age":33}
dict2=dict1.copy()

#Setdefault will add the key and value provided if key is not present already, if already present consider the given value and not the default value
dict1.setdefault("city","Chennai")

#create a dictionary with the keys from list and value from the second argument
dict1={"custid":1,"fname":"Arun","age":33}
dict1.fromkeys(["country","cntry"],"Ind")

#Day 5

print("Tuples (immutable?)")
#Definition of Tuple:Tuple is an indexed sequenced collection of hetrogeneous elements, tuples are immutable (non updatable and non resizable)
#Notation is ()
tup1=(1,"Anirudh",10000,"Chennai")

#select/access
#City where Anirudh present
city=tup1[3]
#count of some element in the given tuple
print(tup1.count("Chennai"))
#search for some element in the given tuple to identify the index
print(tup1.index('Anirudh',0,2))

#Resizable? No (insert/delete)
#Try to Add some elements to the tuple, lets try to add age of Anirudh
#Insert/Append? No
tup2=(30,"Guindy")
tup3=tup1.__add__(tup2)#We can't resize a given tuple, rather we can create a new tuple
print("tuple1 is still not resizable")

#delete? No
#tup1.__delattr__(name="Chennai") #cannot delete the elements of tuple

#Modify (update) - Not possible
tup1=(1,"Anirudh",10000,"Chennai")
#tup1[2]=tup1[2]+1000 #Updating a tuple is not possible

#I want to achieve Insert/update/Delete in a tuple? Not possible by default,
# but we can do some workaround to achieve it? convert to list , do insert update delete and convert back to tuple
tup1=(1,"Anirudh",10000,"Chennai")
tup2=(30,"Guindy")
tup1_lst=list(tup1) #Convert to a list
tup2_lst=list(tup2) #Convert to a list
#Do all operations/functions that list supports (#Other functions to apply)
#Insert
tup1_lst.extend(tup2_lst)
tup1_lst.append(9830303010)
print("Extended/appended tuple list is ",tup1_lst)

#Update
tup1_lst[2]=tup1_lst[2]+1000
print("Salary updated tuple list is ",tup1_lst)

#Delete
tup1_lst.remove("Chennai")
print("City is deleted ",tup1_lst)

#Convert the list back to tuple
tup1=tuple(tup1_lst)


print("Set (mutable) (least important)- Notation {} - "
      "Set is a sorted and distinct collection of iterable elements, cannot be accessed using index ?? Why?")
set1=set({10000,25000,15000,10000,50000})
#how to access the element of a set (cant be access directly by using index/key/values)- Index can't be used why?
#The number of elements/items in the set is not fixed in the numbers or sort order
#set1[0] #not possible to access using index

#set is iterable?yes
for i in set1:
    print(i)

#set is mutable?Yes
#add will help add/update an element not the set
set1={10000,25000,15000,10000,50000}
print("original set",set1)
set1.add(20000)#insert 20k if not present
print("added set with an element",set1)

#update will help add/update another set
set2={25000,35000,45000}
set1.update(set2)
print("updated set with another set",set1)

#set is mutable (resizable) - Removing/popping/cleaning
set1.remove(25000)
print("given element removed set is",set1)

set1.pop()
print("arbitrary element removed set is",set1)

#set is supported with set operation (If we use set, we use it for these purposes)
#Requirement of identifying the common department in the given lists
lst1=['IT', 'HR', 'IT', 'MKT']
lst2=["IT","MKT"]
st1=set(lst1)
st2=set(lst2)
lst3=list(st1.intersection(st2))
print("Common departments between 2 sets, converted to list=",lst3)
st1.intersection_update(st2)
lst4=list(st1)
print("Common departments between 2 sets=",lst4)

st1={'IT', 'HR'}
st2={"IT","MKT"}
#Set operations (special functions)
#Union - combine both the sets
st3=st1.union(st2)
print("Unique Merged departments between 2 sets",st3)

#intersect - combine both the sets
st3=st1.intersection(st2)
print("Common departments between 2 sets",st3)
st1.intersection_update(st2)
print("Common departments between 2 sets",st1)

#difference (difference/subtract/minus) - find the difference between the sets
st1={'IT', 'HR'}
st2={"IT","MKT"}
st3=st1.difference(st2)#subraction of set1 items with set2 items and return result of set1 item
print("subtracted result of set2 from set1 stored in set3",st3)
st1.difference_update(st2) #set1 will be updated with the result of set1 minus set2
print("subtracted result of set2 from set1 updated in set1",st1)
st1={'IT', 'HR'}
st2={"IT","MKT"}
st1.difference(st2).union(st2.difference(st1))#Equivalent of symmetric_difference
st3=st1.symmetric_difference(st2)#subraction of set1 items with set2 and vice versa and return result of both unioned
print("subtracted result of set2 from set1 stored in set3",st3)

st1.symmetric_difference_update(st2)#subraction of set1 items with set2 and vice versa and return result of both unioned updated with set1
print("subtracted result of set2 from set1 stored in set1",st1)

st1={'IT', 'HR'}
st2={'ORD',"MKT"}
print("Help us check whether there is (any common values between both sets, if so return true else false) any one intersection between set1 and set2",st1.isdisjoint(st2))

st1={'IT', 'HR','MKT'}
st2={'IT','MKT'}
print("subset Help us check whether the given set st1 is a child of the set st2 of other",st1.issubset(st2))
print("superset Help us check whether the given set st1 is a parent of the set st2 of other",st1.issuperset(st2))

print("Usecase3 : Complex Tuple - tuple(familyid:int,familyname:str,familymembers:list[dict{k:v,k:v,k:dict{k:v,k:v}}])")
#Understanding the complex type:
#StructType in spark
#Tuple(int,str,list(
# dict(str:str,str:str,str:dict(str:str,str:str))))
# dict(str:str,str:str,str:dict(str:str,str:str)))
# dict(str:str,str:str,str:dict(str:str,str:str,str:str)))
# dict(str:str,str:str,str:dict(str:str,str:str,str:bool)))
complextup=(1,
            "Madison's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}])

#Understand the data structure of the given data
#tuple(familyid:int,familyname:str,familymembers:list[dict{k:v,k:v,k:dict{k:v,k:v,...}}])
#Try to parse one after another
print("id is ",complextup[0])
print("Family name is ",complextup[1])
print("gender of first list element is ",complextup[2][0]["gender"])
print("relation of first list element is ",)
print("personalinfo of the first list element is ",)
print("personalinfo title of the first list element is ",complextup[2][0]["personalinfo"]["title"])
print("personalinfo name of the second list element is " ,)
print("personalinfo hobby of the third list element is " ,)
print("personalinfo schooling info of the fourth list element is " ,)