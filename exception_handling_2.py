#EXCEPTION HANDLING
#Understanding of Exception: what, exception handler blocks (try,except,else,finally)
#Exception handling methodologies: Block level or Statement level
#Types of Exception: Predefined (TypeError, ValueError, KeyError,DivideByZero,IndexError,FileNotFound..)
# & Userdefined/CustomExceptions
#importance - Dataengineer less (already framework spark or any other handled the exceptions)
#importance - python developer higher important (application/framework/tool/automation),
# medium (already framework spark handled the exceptions)
#What? - Exception is a error occurrs when the program is executing at any stage for any
# reasons (data error, name/key/value error, type error, environment error, file not found, format error)
# and makes the flow of program terminated abruptly (out of control)
# Exception Handler (graceful handling of program termination by generating logs, messages, alternative codes, releasing of resources, closing of connections)
# help us handle or take the control from the line where main program got terminated - is a construct/code/class (except)
# that help us handle the state of exception
#Example:
#exception->exceptional cases, unexpected events, unusual, abnormal..
#1. try - I am going to a store to buy something to my home (plan it perfectly to avoid any unexpected events)
    #take a vehicle
    # go to shop,
    # add different items in the cart,
    # pay the bill,
    # take a vehicle
    # come back home
#2. except - any unexpected event occurs, handle it accordingly
    #exception1 - trip got cancelled because of some other priority work came
    #exception2 - vehicle is not starting, but i may use some other vehicle or go by walk or call the mechanic and abort my journey
    #exception3 - shop is closed
    #exception4 - some products are not available...
    #exp5- card declined/not accepted or wallet is lost
    #exp6 - vehicle is not starting
    #exp7 - something went wrong which i didn't predicted (expect unexpected)
#3. else - (If except doesn't happened) If I am not getting any exception, what I have to do then?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
#4. finally (If 1+3 or 1+2  happened) If I am not getting any exception or I got some exception, what I have to do?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
    #plan for some other alternative journey

try:
    a="ten"
    if isinstance(a,int):
     print("a is int")
    else:
     print(len(a))
    b=10/0#exception
    print("If any error occurs in above line of line# 4, this print will not happen, bcz python moved the control out")
except Exception as errmsg:
    print("some exception occured - ", errmsg)
    b = 10 / 1
    print(b)
else:
    print("i will be executing if no exception occurs")
finally:
    print("i will be executing at any cost whether exception occurs or not")


print("b. Types of exception handling - Predefined exception - When we anticipate the possible exception may happen which is already defined by python")

try:
    filenm=input("enter the file to open \n")
    #/home/hduser/sparkdata/file2.json
    openfile=open(filenm,'r')#FileNotFoundError
    offer_pct_num = int(input("Enter the numerator for the offer"))
    offer_pct_den=int(input("Enter the denominator for the offer"))
    #assert offer_pct_den==100,"Denominator has to be 100 only" #Assertion error (custom exception + predefined)
    #price = input("Enter the price")
    products_lst=["laptop","mobile","keyboard"]
    choose_product=int(input("choose the product from the list"))#Value error
    products_price_lst=[100000,15000,400]
    print("price for the product is",products_lst[choose_product])
    print("price for the product is",products_price_lst[choose_product])#IndexError
    #print(products_lst[choose_product].concat(products_price_lst[choose_product]))
    price=int(products_price_lst[choose_product])#Value error
    #print("total amount is "+price)#type error
    total_price = price - (price * (offer_pct_num / offer_pct_den))  # zerodivideerror
    products_lst_dict={"laptop":100000,"mobile":15000,"keyboard":400}
    choose_product=input(f"choose the product from the dict {products_lst_dict} \n")
    price=products_lst_dict[choose_product]#Keyerror

    total_price=price-(price*(offer_pct_num/offer_pct_den))#zerodivideerror
    print("Total amount to pay is ",total_price)

except FileNotFoundError as err:
    print("enter the right filename - ",err)
except AssertionError as err:
    print("Assertion error (custom exception + predefined) ",err)
except ValueError as err:
    print("enter the right value of integer - ",err)
except IndexError as err:
    print(f"enter the maximum index value of {len(products_price_lst)-1}",err)
except TypeError as err:
    print("Type error occured - ",err)
except ZeroDivisionError as err:
    print("Denomiator should not be zero",err)
except ArithmeticError as err:
    print("some arithmetic exception occured in the program",err)
except KeyError as err:
    print(f"Enter the right key {products_lst_dict.keys()}", err)
except Exception as err:
    print("Some exeception occured - ", err)


print("c. Types of exception handling - Userdefined exception - If python doesn't provided some exception which we wanted to create and use ")
class WE43CustomException(Exception):
    print("Some custom exception program we created")
    print("if customer choosen option > 9 in IVR, then route the call to the customer care executive")


try:
    ivr_option = int(input("Enter the option to choose\n"))
    if ivr_option > 9:
        raise WE43CustomException
    print("program completed successfully")

except WE43CustomException as err:
    print("our custom/userdefined exception occured", err)

print("d. Methodologies of Exception handling - block or statement level exceptions")
#Block level Exceptions - If a program get an exception in any line/statement of the code, the entire block will be aborted (So far what exception handler programs created)

print("Block level Exception")
try:
    a=10
    print(len(a))# IF Exception occurs in this line, the rest of the loc in this block will not be executed (BLOCK LEVEL )
    print("If any error occurs in above line of line# 2, this print will not happen, bcz python moved the control out of this block")
    b=10/0#exception occurs
    print("If any error occurs in above line of line# 4, this print will not happen, bcz python moved the control out of this block")
except Exception as errmsg:
    print("some exception occured - ", errmsg)

print("Statement level Exception")
#Statement level Exceptions - If a program get an exception in any line/statement of the code, the entire block will be not aborted, rather the program will continue
try:
    a=10
    print("statement1")
    print(len(a))# IF Exception occurs in this line, the rest of the loc in this block will not be executed (BLOCK LEVEL )
except Exception as errmsg:
    print("some exception occured - ", errmsg)
try:
    print("statement2")
    print("If any error occurs in above statement 1, this print will happen, bcz of statement level exception")
    b=int("hello")#exception occurs
except Exception as errmsg:
    print("some exception occured - ", errmsg)
    exit()
try:
    print("statement3")
    print("If any error occurs in above statement2, this print will happen, bcz of statement level exception")
    b=10/0#exception occurs
except Exception as errmsg:
    print("some exception occured - ", errmsg)