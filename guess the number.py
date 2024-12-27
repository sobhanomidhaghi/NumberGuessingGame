import random

try:

    low=int(input("enter lower bound:\n"))
    high=int(input("enter high bound:\n"))
except:
    print("please enter a valid number ")
r=random.randint(low,high)
guess_count =5
while guess_count>0:
        try:
            new_guess_str=input(f"remained guess:{guess_count}=> Enter your next guess:\n")
            new_guess=int (new_guess_str)
            if r==new_guess:
                print("Great! your guess is corecct " )
                break
            elif r>new_guess:
                print("your guess is low than selected number")
            else:
                print("your guess is higher than selected number ")
                guess_count-=1
        except: 
             print("please enter a valid number")
