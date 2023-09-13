# sign in
from curses import BUTTON_ALT
from logging import root
from unittest import result


print("Hello! Are you ready to organize your batches of money?")
input(" " " Type YES if so: " " ")

email= input("What is your email?")
password= input("What is your password?")
income= int(input(" " "What is your monthly income? kd" " "))

name= input("what is your name? ")
age= int(input("what is your age? "))
if age >= 18:
    print(f"Hello. Welcome {name}! ")
    print("Welcome to this app where you are able to save your savngs and investments while organizing your expences at the same time.")
    print("You are also able to enter specific amounts of money into your personalized categories that you make.")
    print("For example, you can make personalized categories and put in how much you want to save for this category in each month.")
    print("After you have done this, the app will automatically save the amount of money you chose to save for each month from your account into these categories.")

else:
    print("You should wait.")

#storage

print("We offer these services.")
saving_option= print("You get to list savings you wish to save and investments you want to invest in.")
print(" " "Having one of these saved is mandatory since it is a special feature of out app." " ")
saving_options= ("W", "E", "G")
print("What do you want to save for?")
print("W= Water Bills")
print("E= Electrical Bills")
print("G= Gas Bills")

user_option= input("Enter an option: ")
option_input= float(input("How much would you like to save monthly for this bill?"))
print("This is how much you will invest for each month depending on your chosen amount for investements.")
print(("%.2f")% (option_input/income * 100))



def savings1():
    savings= input("What would you like to save for? ")
    savings_user_input= float(input("How much would you like to save from your income for each month? kd"))
    print(" " " This is how much you will save for each month depending on your chosen amount for savings." " ")
    print(("%.2f")% (savings_user_input/income * 100))

def investments2():
    investments= input("What would you like to invest for? ")
    investments_user_input= float(input("How much would you like to save from your income for each month? kd"))
    if investments_user_input >= 80:
        print(" " " This is how much you will invest for each month depending on your chosen amount for investements." " ")
        print(("%.2f")% (investments_user_input/income * 100))
    else:
        print("To invest you should have kd80 or more. Try saving.")
        print(savings1())

print("1= Savings")
print("2= Investments")
user_option1= int(input("Are you interested in 1(savings) or 2(investments)?"))

if user_option1== 1:
    print(savings1())
elif user_option1== 2:
    print(investments2())

#confirmation 

user_entered_approval= input("Type S if you are set with your decisions: ")
if user_entered_approval == "S":
    print("Your decisions have been approved. We will notify you each month whenever an amount is taken from your income.")
else:
    user_option2= int(input("If you would like to organize savings or investments again, enter 1(savings) or 2(investments)."))
if user_option2== 1:  
    print(savings1())
elif user_option2== 2:
    print(investments2())

else:
    print("Thank you for trusting us, you can come back anytime!")
