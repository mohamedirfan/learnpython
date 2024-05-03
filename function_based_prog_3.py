#day 7
'''
What is a Function? Our Aspirant's response
Function/method/procedure/module/subroutine/stored program...
pre-defined (It work in certain way)/adhoc/anonymous/partial process to reuse
for an input then specific work performed (Execution of set of steps) gives an output which can be Reusable
or
grouping line of code to perform a specific task for reuse
or
orchaestrated sequence of actions
or
modular programming to break the complexity and reusable code /segregatee the code for ease of use
'''
import sys


def compname(case):
    if case=='u':
        company_name="Inceptez".upper()
    elif case=='l':
        company_name = "Inceptez".lower()
    else:
        company_name = "Inceptez"
    print(company_name)
    #return company_name

company_name="Inceptez"

import python.learning.allfunctions
print(python.learning.allfunctions.compname('u'))

#FUNCTION BASED PROGRAMMING (Python is a pure FBP Language) - Rather than reinventing the wheel reuse it..
#What is a FBP - If we are giving high priority for functions as like variables and use functions in most of our programming rather than rewriting the
# functionalities again and again reuse it for reducing the complexity.
# Simply say, FBP will help us convert our prog lang to high level (10 lines of code)
# rather than low level (boiler plate coding 100 lines of code)
#FBP will reduce the complexity of doing boiler plate coding (low level programming Cobol/Java/cpp)?
#Python is a FBP (not a boiler plate programming rather it is a high level programming)

#What is Functions/Methods in FBP - Functions/methods/procedures/modules/subroutine..
#A function/method is a collection/group of statements/loc that perform a certain task
#Function/Method is a collection of statements/code/lines of program for performing a common functionality with or without output is produced as a result
#Functions are used to put some common and repeated task into a single name, so
#instead of writing the same code again and again for different inputs, we can simply call the (name along with some arguments) function.

#Features of Functions in Function Based Programming
#1. Concurrency - Calling the same function at the same time from different programs/environments/platform
#2. MultiThreading/Parallelism - The function that runs in parallel at the same time to provide the desired result as per the input passed.
#3. Distributed - The function that runs in parallel at the same time to provide the desired result as per the input passed across multiple workarea (memory containers/nodes)
#4. Simple/Elegant to use, easy for consumption and reasoning out..

#FBP – Characteristics
#Functions are first class citizens - Functions are given equal priority as like varibles
#In a Python programming language a variable can act differently
#1. A variable can hold values
a=100
#2. A variable can be local or global
global var1
var1=200

#3. A variable can refer the data kept in memory or another program that is loaded in memory
#rdd1=sc.parallelize(list(data),4).map(met1) #rdd refers the data in the memory
#spark #holds program reference of SparkSession in memory

#4. A variable can hold functionality (A function is equally considered as a variable in FBP)
a=lambda input:input+100#quick anonymous randome functationality achieved in a variable
print(a(100))
print(a(200))

#Functions are composable - to achive complex output, we don't have to create a complex function rather we can call/compose simple functions
compname="IncEpTez"
compname.lower().index('t')

#Functions are not time bounded (stateless or no side effect) - We can call functions any number of times
#Below anonymous code is a time bounded (call the same logic will vary based on how many times you call)
a=1
if a>=1:
    a=a+1
print(a)

#If i convert the above code into a function, it will become non time bounded (call the function any time the result will not vary)
def met1():
    a=1
    if a>=1:
        a=a+1
    return a

print(met1())
print(met1())

#Functions are simple to create/manage/call
#Once for all effort for creation
#manging is easy in one place, changing the functionality in one place will affect every where, so easy of modification in an application
#calling is also easy to perform just by knowing the signature of the function

#Why we need to create Functions or why we need FBP -
#1. Functions can be created once and reused multiple times
#2. Functions are used to call/run in a parallel (I have 1000 rows, running a function in 10 parallel threads with each thread handles 100 rows)
# and in concurrent fashion (I am calling a single function at the sametime from 10 diffent applications/programs)
#3. Functions help us reduce the LOC by reusing and by composing
#4. Functions are used for creating Application specific Reusable Frameworks (Masking FW, DMA FW, Metricbot, DQ FW etc.,)
# Generic Frameworks (Spark/Airflow/glue) or custom functionalities (udf, custom functions, Cloud functions) or
# centralized functionalities (If we change the function in one place, that affects the entire consuming applications of the given functions eg. change in profit ratio in one place)

#All about Functions or Methods in FBP - syntactically...
###################################################
#1. How to Create a function and call a function (High level)
#If I create a function in a variable then we call it as function
#If I create a function starting with def keyword then we call it as method
#but both method or functions can be pronounced interchangably (u can name it in anyway both are correct)

#1. Minimal/least way of creating a method
def method_name():
    pass

#2. Regular/Optimal/typical/formal way of creating a method
def gen_mailid(fname:str,lname:str):#arguments are optional
    '''This function help you generate mail id of the new joinees'''
    mailid=fname+'.'+lname+'@inceptez.com' #A line of code of anything like pass/return/print/variable/functioncall...
    print(mailid)#optionally we can print something to understand the execution the function
    return mailid #optionally we have returns in functions
print(gen_mailid("mohamed","irfan"))

#We need to have a def keyword (definition of a function) - Mandatory
#followed by the function name - Mandatory
#followed by argument(s) - Optional,
# followed with datatype mentioned (to help us understand the datatype signature of the method)- Optional
# mentioned inside the brackets() - Mandatory
#followed by ':' (completion of the definition) - Mandatory
#followed by - some description in ''' , to display the methods description when hover- Optional
#followed by the body of the program (one/multiple lines of code - core logics + std output + return) - Mandatory (atleast a single line of any or all of them)
#followed by return keyword - where as return help us send back result to the calling environment - Optional

#3. What are the possible way of creating functions/methods
#all permutation and combination works...
#a.Method with no input arguments and no return - truncate tablename;
def cleanup_tmp_space():#A method to call daily to clean a predefined /tmp folder in an OS
    folder_to_clean='/tmp'
    print(f"deleting the temporary {folder_to_clean} folder (hardcoded)")

#Let us call the above functions with appropriately...
cleanup_tmp_space()

#b.Method with input arguments and no return - delete from tablename where city='chennai';
def cleanup_some_space(folder_to_clean):#A method to call daily to clean a the given folder in an OS
    print(f"deleting the temporary {folder_to_clean} folder (parameterized/argumented)")

#Let us call the above functions with appropriately...
cleanup_some_space('/home/hduser/irfan/')

#c.Method with no input arguments but return - select count(1) from tablename;
def cleanup_tmp_space_return_total_files_cleaned():#A method to call daily to clean a predefined /tmp folder in an OS and return the number of files deleted
    folder_to_clean='/tmp'
    print(f"deleting the temporary {folder_to_clean} folder (hardcoded)")
    return 42#the number of files deleted

#Let us call the above functions with appropriately...
print(cleanup_tmp_space_return_total_files_cleaned())
somevariable=cleanup_tmp_space_return_total_files_cleaned()
if somevariable>40:
    print("cleaned huge content")
else:
    print("cleaned minimum content")


#d.Method with input arguments and return - select count(1) from tablename where city='chennai';
def cleanup_some_space_return_total_files_cleaned(folder_to_clean):#A method to call daily to clean a given folder in an OS and return the number of files deleted
    print(f"deleting the temporary {folder_to_clean} folder (hardcoded)")
    return 42#the number of files deleted

#Let us call the above functions with appropriately...
print(f"mail - the total files cleaned today is {cleanup_some_space_return_total_files_cleaned('/home/hduser/irfan/')}")

#4. How do we call the Methods:
#How to just print the output of a function
print(f"{cleanup_some_space_return_total_files_cleaned('/home/hduser/irfan/')}")

#How to store the output of a method and use that output further
somevariable=cleanup_tmp_space_return_total_files_cleaned()
if somevariable>40:
    print("cleaned huge content")
else:
    print("cleaned minimum content")

'''def fun_recon(df_world_sql,df_tabledata):
	src_cnt=df_world_sql.count()
	tgt_cnt=df_tabledata.count()
	if (src_cnt==tgt_cnt):
		#print("Data loaded into hive table successfully")
        return True
	else:
		#print("Data not loaded into hive table successfully, hence reloading")
		#df_world.write.mode("overwrite").saveAsTable("raw.weblog_world")
        False


recon_flag=fun_recon(df_world_sql,df_tabledata)
if recon_flag:
    print("Data loaded into hive table successfully")
else:
    print("Data not loaded into hive table successfully, hence reloading")
    # df_world.write.mode("overwrite").saveAsTable("raw.weblog_world")
#df_tabledata=spark.read.table("raw.weblog_world")
#fun_recon(df_world_sql,df_tabledata)
'''

#module.py arg1 -> function(arg1)

#How to pass an argument to the function using a derived local value or hardcoded value
dir_to_delete='/home/hduser/irfan/'
dir_to_delete=input('provide the directory to delete')
#dir_to_delete=sys.argv[1]
cleanup_some_space_return_total_files_cleaned(dir_to_delete)

#Call the method with one argument value passed, if not it will fail typically
cleanup_some_space_return_total_files_cleaned('some argument')

#or in other hand the method can still run if we don't pass arguments (provided if the method is a default argument method)
def cleanup_some_space_return_total_files_cleaned(folder_to_clean='/tmp'):#A method to call daily to clean a given folder in an OS and return the number of files deleted
    print(f"deleting the temporary {folder_to_clean} folder (hardcoded)")
    return 42#the number of files deleted

cleanup_some_space_return_total_files_cleaned()

#completed the Swiggy usecase by creating a formal method->
# keep this program inside the method and call it as a method including exception handling implemented inside the method
def swiggy_dynamic_pricing_method(cart_price:int, company_fixed_value_march):
    '''Swiggy Usecase for calculating the dynamic pricing of the product'''
    try:
        min_pur=int(company_fixed_value_march["min_puchase"])
        if cart_price <= min_pur:
            print(f'No Offer is applied, cart price should be greater than {min_pur}')
            #print(f'Final Amount to be paid ', cart_price)
            return cart_price
        else:
            off_percent = cart_price * (float(company_fixed_value_march["off_pct"] / 100))
            max_of = int(company_fixed_value_march["max_off"])
            if off_percent > max_of:
                print(f'Maximum Offer {max_of} is applied')
                fin_amt=cart_price - max_of
                #print(f'Final Amount to be paid {fin_amt}')
                return fin_amt
            else:
                applied_off=round(off_percent)
                print(f'Applied offer is {applied_off}')
                fin_amt=cart_price - applied_off
                #print(f'Final Amount to be paid {fin_amt}')
                return fin_amt
    except Exception as err_msg:
        print(f"Error applying offer to the Cart price"
              f"is : {err_msg}")

company_fixed_value_march={"max_off":100,"off_pct":10,"min_puchase":500}

final_price=swiggy_dynamic_pricing_method(300,company_fixed_value_march)
print(f'Final Amount to be paid {final_price}')

#5. How to create & call the methods using different Argument types: Important part
##############################################################################
#Different type of methods/functions arguments are there -
# positional arg func, named/keyword arg func, default arg func, arbitrary arg func, keyword arbitrary argument function

#Lets take an example of calculating bonus and incentive for our employees of a dept
#Let's create a common method to calculate bonus and incentive applied salary of our different dept employees
it_emp=[10000,20000,15000]
mkt_emp=[40000,10000,35000]
def calc_sal_bon_inc(sal,bon):
    inc=1000
    total_sal=sal+(sal*(bon/100))+inc
    return round(total_sal)

for sal in it_emp:
    print(f"total sal for the given {sal} is {calc_sal_bon_inc(sal,10)}")

#A. Positional arguments methods
print(calc_sal_bon_inc(10000,15))#We have to position our input following the same order of arguments defined in the method
print(calc_sal_bon_inc(15,10000))#If we follow a wrong order the result will be impacted

#B. Named/Keyword arguments methods
#calling the named arguments methods by passing the arguments assigning with the respective names in any order/position
print(calc_sal_bon_inc(sal=10000,bon=10))
print(calc_sal_bon_inc(bon=15,sal=10000))

#c. Default arguments methods -
# Default arg func/met will help us define the funct with some default args, if the given arg is not passed by the calling environment,
# then default value will be used
def calc_sal_bon_inc(sal=0,bon=10):
    inc=1000
    total_sal=sal+(sal*(bon/100))+inc
    return round(total_sal)
print("positional with default arguments")
print(calc_sal_bon_inc(10000,15))#only positional is used here
print(calc_sal_bon_inc(10000))#positional with default argument func(10000,10)
print(calc_sal_bon_inc(15))#(will not work) positional with default argument result wrongly func(10) here salary will be considered as 15 and bonus as 10
print("to resolve the above issue, we need to use both named with default arguments")
print(calc_sal_bon_inc(bon=15))

print("Usage of only default arguments")
print(calc_sal_bon_inc())#only default arg method func(0,10)

print("named with default arguments")
print(calc_sal_bon_inc(sal=10000,bon=10))#only named is used here...
print(calc_sal_bon_inc(sal=10000))#named with default
print(calc_sal_bon_inc(bon=10))#named with default

#d. Arbitrary (any numbers) Argument Method/Function - Accepts the argument as tuple with the notation of *argument_name
# If we are not sure about the number of arguments that we are going to pass to this method, but we use the same order (position) of passing the arguments
#sal,bonus,incentive=1000
print("d.Arbitrary Argument Function/Method")
hcl_emp=[20000,20000,15000]
cts_emp=[30000,20000,15000,2000]
cts_bon=10
cts_inc=2000
acc_emp=[40000,10000,35000]
acc_bon=12
#arbitrary (any/random/multiple) arguments function
print("calling arbitrary argument function for sal, bon, inc calculation....")
def third_party_calc_sal_bon_inc(*args):#*args represents this method can be passed with any number of positional arguments
    print(type(args))#tuple because the argument can be hetrogenous in type and it can have duplicates
    len_args=len(args)
    if len_args>=3:
        print("cts")
        inc=args[2]
        bon=args[1]
        sal=args[0]
        total_sal=sal+(sal*(bon/100))+inc
        #return round(total_sal)
    elif len_args==2:
        print("accenture")
        inc=0
        bon=args[1]
        sal=args[0]
        total_sal=sal+(sal*(bon/100))+inc
        #return round(total_sal)
    elif len_args==1:
        print("hcl")
        inc=0
        bon=0
        sal=args[0]
        total_sal=sal+(sal*(bon/100))+inc
    return round(total_sal)

print(third_party_calc_sal_bon_inc(10000,10,1000))
print(third_party_calc_sal_bon_inc(20000,12))
print(third_party_calc_sal_bon_inc(12,20000))#we have to maintain the position
print(third_party_calc_sal_bon_inc(30000))

#e. Keyword Arbitrary Argument Method/Function - Accepts the argument as  with the notation of **argument_name
# If we are not sure about the number of arguments that we are going to pass to this method and
#the order of the argument we are going to pass is unknown (Named arguments) , we can use keyword arbitrary arg method
print("e. Keyword-Arbitrary Argument Function/Method")

#If we are not going to get bon as an argument, rather we are going to incen

#Usecase: Create a method should take 3 arguments, firstname, lastname, domain to generate mail id
#generate_mail('mohamed','irfan','@inceptez.com') -> mohamedirfan@inceptez.com (if the 3rd is not passed, then return mohamedirfan@gmail.com
def generate_mail(fname,lname,domain='@gmail.com'):
    return fname+lname+domain
#I need to call the above method using all the 3 methodologies we are learning positional, named, default
print(generate_mail('mohamed','irfan','@inceptez.com'))
print(generate_mail(lname='irfan',fname='mohamed',domain='@inceptez.com'))
print(generate_mail(lname='irfan',fname='mohamed',domain='@inceptez.com'))
print(generate_mail(lname='irfan',fname='mohamed'))
#I need to call the above method using additional 2 methodologies we are learning arbitrary and keyword arg functions with default arg function -
# I may pass fullname alone or i may pass fname,lname,@inceptez.com by following the proper order or any order it has to work, use - arbitrary or keyword arguments
def generate_mail(*mailid):
    if len(mailid)==2:
        return mailid[0]+mailid[1]+'@gmail.com'
    elif len(mailid)==3:
        return mailid[0]+mailid[1]+mailid[2]
    elif len(mailid)==1:
        return mailid[0]
print(generate_mail("mohamed","irfan"))
print(generate_mail("mohamed","irfan","@inceptez.com"))
print(generate_mail("mohamedirfan@gmail.com"))
generate_mail("mohamed","@inceptez.com")#returns unexpected result, solution is going with keyword argument method
def generate_mail(**mailid):
    if len(mailid)==2:
        return mailid['fname']+mailid['lname']+'@gmail.com'
    elif len(mailid)==3:
        return mailid['fname']+mailid['lname']+mailid['domain']
    elif len(mailid)==1:
        return mailid['fullmailid']
generate_mail(lname="irfan",fname="mohamed")
generate_mail(lname="irfan",domain="@inceptez.com",fname="mohamed")
generate_mail(fullmailid="mohamedirfan@inceptez.com")

#day 8
#6. Special Types of Methods/Functions in Python - Is not much important for creating/implementing the methods by Dataengineers,
#but for understanding the type of methods/functions used in the framework, the below learning is useful.
# FBP (special methods) - Higher Order Function (type1 & type2), Anonymous/lambda/function literal/value function,Closures, recursive functions/tail recursion
# OOPs (special methods)- instance (default), class,static methods
print("**********Special Types of Methods/Functions in Python - Important (interview purpose)***************")
#a. Higher Order Functions - Top priority
print("a. Higher Order Functions - Two Types (HOF1 & HOF2)")
print("Benifits of HOF1 -> 1. We can use the functions seperately or along with other functions "
      "2. Rather than rewriting the code in a given function we can reuse it by passing the function as an argument ")
#1. Type1 Higher order function says -> If a method takes another method as an input argument

#hof1 - how to understand what is hof in a simple way syntactically...
def met2():
    return "method2 return value"
def met1(some_method_as_input):#HOF1 - met1 is a HOF1 because it takes an input of another met2
    print(some_method_as_input())
met1(met2)#met1 is a higher order method of type1

#Realtime example : Calculate the salary of our employees based on working days
def calc_sal(salperday,workingdays):#Is this is a HOF? Not a HOF
    days_to_reduce=31-workingdays#Can HR dept use this functionality seperately? No
    sal_to_reduce=salperday*days_to_reduce
    return (salperday*31)-sal_to_reduce

#How to convert the above method into HOF and what is the benifits of doing it?
def calc_workdays(workingdays):
    days_to_reduce=31-workingdays
    return days_to_reduce

def calc_sal(salperday,workingdays,method1):#Is this is a HOF1? Yes, because we are passing a method calc_workdays as an argument
    days_to_reduce=method1(workingdays)
    sal_to_reduce=salperday*days_to_reduce
    return (salperday*31)-sal_to_reduce

print(f"HR Sending a mail to the supervisor about the days the given employee didn't worked for a given month {calc_workdays(20)}")
print(f"Finance Depositing the final salary for the given employee in bank {calc_sal(1000,20,calc_workdays)}")

#Usecase to understand HOF1: Create a calculator method that should take add/sub/mul/div method as an input argument
def add(a,b):
    return a+b

def simple_calc(a,b,met1):#this is a HOF1
    if met1==add:
        result=met1(a,b)
        return result

#2. Type2 Higher order function HOF2 says - If a method returns another method as a return type then it is HOF2
#Other names for the HOF type2 -
#hof2 - how to understand what is hof2 in a simple way...
def wrapper_method(what_met_u_want_to_return):
    if what_met_u_want_to_return=='m2':
        def met2():
            return "met2 is called"
        return met2#The met2 object/code/functionality/logic (BUT NOT VALUE) is returned
    else:
        def met3():
            return "met3 is called"
        return met3#The met3 object/code/functionality/logic (BUT NOT VALUE) is returned

another_function=wrapper_method('m2') #partial functionality i am getting
#now another_function holds what? met2 code
print(another_function()) #equivalent to call met2()

#Why HOF2 is otherwise called as - Hierarchical or nested method/partial methods/currying function
def veg_curry():
    def spice(arg):
        return "half cooked curry "+arg
    return ("half cooked curry",spice)
half_cooked_partial_curry=veg_curry()
half_cooked_partial_curry[1]("pepper")

#Reallife example of HOF Type2 - AC remote (method1) returns mode (method2) is an example of HOF2
#Can you consider this AC remote as an usecase or calculator functionality as an usecase for HOF2?

def scientific_calc(calc_type,op_type):#this is a HOF2
    if calc_type=='simple':
        if op_type=='add':
            def add(a, b):
                return a + b
            return add
    elif calc_type=='scientific':
        import math
        if op_type=='sin':
            def sin(a):
                return math.sin(a)
            return sin

print("b. Closures Functions")
print("What is closure? If the result of a given method is changed/affected by the value defined outside of the given function ")

#Simple function
def calc_bonus(sal,bon):
    return sal+bon
print(calc_bonus(10000,1000))

#Closure Functions (simple understanding)- below calc_bonus method is affected by some values/variables defined outside of the function
bon=1000
def calc_bonus(sal):
    bon=2000
    return sal+bon
print(calc_bonus(10000))

#Can you create a method called calc_sal_bonus_incentive using a higher order method 1, 2 and closure concepts?
def all_calc(sal,bon,inc):
    return sal + bon + inc

def calc_sal_bonus_incentive(sal,met1):#hof1
    bon = 1000#closure
    def calc_bonus():
        inc=2000
        return met1(sal,bon,inc)
    return calc_bonus#hof2

print("c. Lambda Function - A function created anonymously or a function as a variable using lambda keyword")
#Lambda functions can be called as function literal/anonymous function/value function
#Interview Question: Diff between methods & functions -
# Method: Any functionalities/store program created with def keyword (syntactically)
def all_calc_method(sal,bon,inc):
    return sal + bon + inc
# Method: Can be used for some common, complex (logic can be in multiple lines) functionality purposes across the modules of an application
from python.learning.common_module import all_calc_method
print(all_calc_method(10000,1000,2000))

# Function: Any simple functionalities/store program created with lambda keyword (syntactically)
all_calc_function=lambda sal,bon,inc: sal + bon + inc
# Function: Can be used for some anonymous, simple (logic should not be in multiple lines) functionality purposes within the given module, not across the module
all_calc_function=lambda sal,bon,inc: sal + bon + inc

#Example of using defined method or anonymous functions?
sal_lst=[10000,20000,5000,15000,25000,50000]
import functools #this module contains reduce function availble
from python.learning.common_module import max_min_sal#We have to go with defined method if complexity is high
max_sal=functools.reduce(max_min_sal,sal_lst)
print("min salary is ",max_sal)

#Above complex logic (with default args, nested if conditions) can't be achived using lambda function, because lambda expects
#the logic as a single expression, regular code will not work...
min_max_func=lambda sal1,sal2:sal1 if sal1>sal2 else sal2 if sal2>sal1 else sal1
#min_max_func=lambda sal1,sal2:
#if sal1>sal2: return sal1 elif sal2>sal1: return sal2 else: return sal1
max_lambda=lambda x,y:x if x+10>y else y

#below is preferred to write, though we are using defined method anonymously (using this method only inside this module for my purpose alone)
def max_min_sal(sal1,sal2,type='min'):#defined method writtened like a lambda function anonymously
    if type=='max':
        if sal1>sal2:
            return sal1
        else:
            return sal2
    else:
        if sal1<=sal2:
            return sal1
        else:
            return sal2

print("d. Recursive Function or tail recursion - A function called by itself repeatedly or recursively")

#Realtime example of Recursive Function? SIP, FD, Complex Interest (interest for interest)
#I am investing 100000 rupees with an return of 10% year over year, after 3 years what is my return?
#100000 -> 100000+10000=110000 (year1) -> 110000+11000=121000 (year2) -> 121000+12100=133100 (year3)
ret=10
def year1(amt):
    return amt+(amt*(ret/100))
year1return=year1(100000)

def year2(year1return):
    return year1return+(year1return*(ret/100))
year2return=year2(year1return)

def year3(year1return):
    return year1return+(year1return*(ret/100))
year3return=year3(year2return)

#Lets write the above function in a single recursive function
retpct=10
def return_of_investment_compount_interest(amt,tenure):
    #print(tenure)
    #print(amt)
    if tenure==0:
        return amt
    else:
        amt=amt+(amt*(retpct/100))
        tenure=tenure-1
    return return_of_investment_compount_interest(amt,tenure)

final_amt=return_of_investment_compount_interest(100000,3)
print(final_amt)
#Some of the interview questions asked in python or any other programming languages?
#Find the given value is prime number or not
#calculate the even or odd values from the given list
#build a pyramid using python
#check whether given value is palindrome
#create fibboneci series 0,1,1,2,3,5,8,13,21 (Agile/Scrum - Sprint planning -story points)
#create factorial of n numbers - fact(4) = 4*3*2*1
#usecase: to calculate factorial or fibboneci series using recursive function?

def fiboneci(i):
    if i==0:
        #print(i)
        return 0
    elif i==1:
        #print(i)
        return 1
    else:
        #print(i)
        #print(fiboneci(i-1)+fiboneci(i-2))
        return fiboneci(i-1)+fiboneci(i-2)

for i in range(0,5):
    print(fiboneci(i))

print("e. Few more special methods/functions in Python OOPs - ")
#There are few more special functions/methods available in Python (Object oriented programming part)

#7. Scope of Variables in Functions/Methods - Local and Global variable
print("7. Scope of Variables in Functions/Methods - Local and Global variable")

print("a. Local Variable - ")

print("b. Global Variable - ")

print("c. Local Variable defined as global - ")
