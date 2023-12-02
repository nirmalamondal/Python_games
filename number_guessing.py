import random
print("welcom to the number guessing game")
computer_guess=random.randint(1,100)
n=int(input("choose a number between 1 and 100\n"))
level=input("choose level hard or easy\n").lower()
if level=="easy":
    attemp=10
elif level=="hard":
    attemp=5
if n==computer_guess:
     print(f"You win the number is {n}")
else:  
    attemp-=1
    if(n>computer_guess):
        print("Too High")
    else:
        print("Too Low")       
    while(attemp):
        print(f"You have {attemp} attempts left to guess the number")    
        number=int(input("Make a guess: ")) 
        if(number==computer_guess):
            print(f"You win the number is {number}")
            break
        elif(number>computer_guess):
            print("Too High")
            attemp-=1
        elif(number<computer_guess):
            print("Too Low")
            attemp-=1
if attemp==0:
    print(f"You Lose The Number is {computer_guess}")    