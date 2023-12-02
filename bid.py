import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid={}
flag=True
while(flag==True):
 name=input("What is ypur name?\n")
 price=int(input("what is your bid?\n"))
 bid[name]=price
 any_one=input("Is there any bidders? Type yes or no\n")
 if(any_one=="no"):
    flag=False
 else:
    os.system("cls")  
mx=0
for key in bid:
    if(bid[key]>mx):
        mx=bid[key]
        winner=key

print(f"Winner is {winner} and the bidding amount is {mx}")    