import random
user_input1=input("Enter your choice\n")
user_input=user_input1.lower()
l=["paper","rock","scissors"]
computer_choice=random.choice(l)
print(f"Your Choice is {user_input}\n")
print(f"computer's choice is {computer_choice}\n")
if(user_input=="rock"):
    if(computer_choice=="paper"):
        print("You Lose")
    elif(computer_choice=="scissors"):
         print("You Win")    
    else:
        print("Draw")
elif(user_input=="paper"):
    if(computer_choice=="paper"):
        print("Draw")
    elif(computer_choice=="scissors"):
         print("You Lose")    
    else:
        print("You Win")   
else:
    if(computer_choice=="paper"):
        print("You Win")
    elif(computer_choice=="scissors"):
         print("Draw")    
    else:
        print("You Lose")         
