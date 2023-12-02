print("Welcome to the treasure hunt")
n=input("you are in a crossroad Which side you like to go left or right?\n")
if(n=="right"):
    print("You fall into a hole Game over!")
else:
    m=input("You are come to a lake. Do you want to wait for boat or swim?\n")
    if(m=="swim"):
        print("The crocodiles are eat you Game over!")
    else:
        c=input("Which door you want to open blue,red or yellow?\n")
        if(c=="yellow"):
            print("congrtulation You win!")
        else:
            print("The beast eat you Game over!")