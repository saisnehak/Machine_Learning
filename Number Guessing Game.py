import random
rand = random.randint(1,100)
print(" welcome to the guessing game🎲🕹")
print(" The game will be continud untill the correct answer is provided , so no worries")
print(" But the numbetr of attempts will be displayed")
print("All the best") 
attempts=0
while True:
    guess = int(input("guess the number:-"))
    if rand == guess:
        print(" hooray! you rocked ")
        break
    elif rand > guess:
        print(f"number you provided {guess}  think higher")
    else:
        print(f" number you provided {guess} think lower")
    attempts +=1
    print(f" your num of attempts {attempts}")