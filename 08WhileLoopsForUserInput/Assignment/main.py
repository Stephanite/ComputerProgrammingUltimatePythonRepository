import random

def is_letter(character):
    if character in "abcdefghijklmnopqrstuvwxyz":
        return True
    else:
        return False

print("number_guesser")
secretNumber=random.randint(1,10)
response=-1
while response!=secretNumber:
    print("guess the secret number")
    response=int(input())
    if response>secretNumber:
        print("too high")
    elif response<secretNumber:
        print("too low")
if response==secretNumber:
    print("correct")

####
print("")

print("number_guesser_with_lives")
secretNumber=random.randint(1,10)
response=-1
lives=3
while response!=secretNumber:
    print("guess the secret number")
    response=int(input())
    lives=lives-1
    if response>secretNumber:
        print("too high")
    elif response<secretNumber:
        print("too low")
    if lives==0:
        print("game over")
        response=secretNumber
