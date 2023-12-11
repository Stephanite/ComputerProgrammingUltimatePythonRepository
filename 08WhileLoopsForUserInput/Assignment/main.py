import random


print("number_guesser")
#secretNumber=random.randint(1,10)
secretNumber=1
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
#secretNumber=random.randint(1,10)
secretNumber=1
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
        response=secretNumber
if response==secretNumber and lives>0:
    print("correct")
elif response==secretNumber and lives==0:
    print("game over")

####
print("")

print("vending_machine")
amountDue=50
response=-1
changeGiven=0
while amountDue!=0:
    print("amount due: ",amountDue)
    response=int(input())
    if response==25 or response==10 or response==5:
        amountDue=amountDue-response
        print("amount due: ",amountDue)
    else:
        pass
    if amountDue<0:
        changeGiven=changeGiven-amountDue
        amountDue=0
    print("change given: ", changeGiven)
if amountDue==0:
    print("fully paid")

####
print("")

print("hangman")
word=input("enter word: ")
letter=0
answer=""
tries=6
while letter :
    print("nope")
    letter=input()
    if letter in word:
        word.append(letter)
        answer.append(letter)
        print(answer)
    else:
        tries=tries-1
        print(letter," is not in word")
if letter in word and len(word)==1:
    print(answer)