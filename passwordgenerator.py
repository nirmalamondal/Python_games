import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G',
            'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','(',')','*','+','_','+','<','>','{','}',',','.']            
digits=['1','2','3','4','5','6','7','8','9','0']
no_letters=int(input("Enter the number of letters you want in your password\n"))
no_symbols=int(input("Enter the number of symbols you want in your password\n"))
no_digits=int(input("Enter the number of digits you want in your password\n"))
password=[]
for i in range(1,no_letters+1):
    password.append(random.choice(letters))
for i in range(1,no_symbols+1):
    password+=random.choice(symbols)
for i in range(1,no_digits+1):
    password+=random.choice(digits)
random.shuffle(password)
password1=""
for i in password:
    password1+=i
print(password1)