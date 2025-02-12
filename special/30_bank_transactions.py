#Challenge: 30-bank_transactions
#Difficulty:  Intermediate
#Prompt:
#- Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user. 

#Gather user input using the `input` function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

#```
#age = input("How old are you?\n")
#age = int(age)
#```

#Here is a sample output:

#```
#Your current balance is
#4000
#What would you like to do? (deposit, withdraw, check_balance)
#deposit
#How much would you like to deposit?
#1000
#Your current balance is 5000
#Are you done?
#yes
#Thank you!
#```

# Your solution for 30-bank_transactions here:

def deposit(dep, bal):
    bal += dep
    print("your current balance is \n" + bal)
def withdraw(amt, bal):
     bal -= amt
     print("your current balance is \n" + bal)
def check_balance(bal):
    print("Your current balance is \n"+ bal)

def bank():
    bal = 4000
    isDone = 'no'

    check_balance(bal)

    while(isDone == 'no'):
        option = input("What would you like to do? (deposit, withdraw, check_balance)").lower()
        if(option == "deposit"):
            dep = input("How much would you like to deposit?")
            withdraw(int(dep), bal)
        elif(option == "withdraw"):
            amt = input("How much would you like to deposit?")
            withdraw(int(amt), bal)
        else:
            check_balance(bal)
        
        isDone = input("Are you done?(yes/no)").lower()
    

bank()


