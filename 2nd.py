'''from timeit import timeit


def myfunc():
    return


def main():
    stmt = "myfunc()"
    setup= "from_main_import myfunc"
    executiontime = timeit(stmt, setup, number=1)
    print("function execution time in sec:","0:0.08f",format(executiontime))


if name == "_main_":
    main()
    '''
#____________________________________________________________________________________________________________________________________
'''name = input()
surname = input()
hrows = len(name)

print("Hollow Rhombus Star Pattern") 
i = hrows
while(i >= 1):
    j = 1
    while(j <= i - 1):
        print(' ', end = '')
        j = j + 1

    k = 1
    while(k <= len(surname)):
        
        if(i == 1 or i == hrows ):
            print('*', end = '')
        elif( k == 1 or k == len(surname)):
            print('/',end="")
            
        else:
            print(' ', end = '')
        k = k + 1
    i = i - 1
    print()    
'''
#____________________________________________________________________________________________________________________________________________-
'''name = input()
s = name.split()
for i in s:
    for j in range(len(i)):
        
            
        if (j==0 or j == len(i)-1):
            print('_',end="")
        
        else:
            print(" ",end = '')
    print(' ',end='')
    '''
#______________________________________________________________________________________________________________________    
'''def printdate(date):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while date:
        div = date // num[i]
        date %= num[i]
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
  

date1=input("enter date:\n")
for i in date1:
    if(i != '/'):
     printdate(int(i))
    else:
        print(i,end="")'''
#___________________________________________________________________________________________________________________________________
'''from itertools import combinations_with_replacement
name = input("Enter your name\n")
len1=len(name)
comb= combinations_with_replacement(['I','M','C','V','X','L','D'],len1)
for i in list (comb):
    print(*i)'''        
#________________________________________________________________________________________________________________________
'''def isChar (c):
    return ((c >= 'a' and c <= 'z')
            or (c >= 'A' and c <= 'Z'))
  
def isDigit (c):
    return (c >= '0' and c <= '9')
  
def is_valid( email):
    if (not isChar(email[0])) :
          return 0
    At = -1
    Dot = -1
  
    for i in range (0,len(email)):
        if (email[i] == '@'):
             At = i
        elif (email[i] == '.'):
             Dot = i
  
    if (At == -1 or Dot == -1):
        return 0

    if (At > Dot):
        return 0
    return not(Dot >= (len(email) - 1))

  

email = input("enter the mail:\n")
ans = is_valid(email)
if (ans):
    print("VALID MAIL") 
else:
    print("INVALID MAIL")'''   
#___________________________________________________________________________________________________________________________________
'''def solve(name):
  rows=len(name)
  n=1    
  k = 2 * rows - 2  
  for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2    
    for j in range(0, i + 1): 
        if (len(str(n))==1):
            print('0'+str(n), end=" ") 
        elif(n>9):
            print(n,end=' ') 
        n+=1
    print("")  
name=input("Enter yor name\n") 
solve(name)'''    
#______________________________________________________________________________________________________________________________ 
name=input("enter Your name\n")
sum=0
for i in range(0,len(name)):
    sum+= ord(name[i])
print(sum)    
