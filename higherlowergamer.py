from random import random
import random
from game_data import data 
import os
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
def solve(account):
    account_name=account["name"]
    account_desc=account["description"] 
    account_country=account["country"]  
    return (f"{account_name} a {account_desc} from {account_country}") 
def check_answer(guess,a_follower,b_follower):
    if a_follower>b_follower:
        return guess=="a"
    else:
        return guess=="b"    

print(logo)
score=0
flag=True
account_b=random.choice(data)
while(flag):
    account_a=account_b
    account_b=random.choice(data)
    while(account_a==account_b):
        account_b=random.choice(data)
    print(f"Compare A:{solve(account_a)}")  
    print(vs)
    print(f"Against B:{solve(account_b)}")  
    guess=input("Who has more follower? Type A or B: ").lower()
    a_follower=account_a["follower_count"]
    b_follower=account_b["follower_count"]
    is_correct=check_answer(guess,a_follower,b_follower)
    os.system("cls")
    print(logo)
    if(is_correct):
        score+=1
        print(f"You are Right Your current score is {score}")
    else:
        flag=False
        print(f"Sorry You Lose! Your final score is {score}")    



