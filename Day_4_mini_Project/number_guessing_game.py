import math
import random

print("______Welcome to Number Guessing Game_____")
print("____Please choose the range of number you want to guess.____ ")
lower_bound = int(input("Enter the Lower bound:_"))
upper_bound = int(input("Enter the Upper bound:_"))
print(f'You will have to guess the number range from {lower_bound} to {upper_bound} .')

x = random.randint(lower_bound,upper_bound)
number_of_guess = math.ceil(math.log(upper_bound - lower_bound + 1, 2))
print(f"You are given {number_of_guess} chances to guess the number.")

Flag = False
count = 0


while count < number_of_guess:
    count+=1
    
    guess = int(input("Enter your guessed number: " ))
    
    if x == guess:
        print("Congratulations you did it in ",
        count, " try")
        flag = True
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
if not Flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")