def calculator():
 def calculation(a,operators,b):
    if(operators=='+'):
        result=a+b
    elif(operators=='-'):
        result=a-b
    elif(operators=='*'):
        result=a*b  
    elif(operators=='/'):
        result=a/b
    return result
 a=int(input("enter first no\n"))
 operators=input("enter operation you want to perform--\n")
 b=int(input("enter second no\n"))   
 result=calculation(a,operators,b)     
 print(f"your result is {result}") 
 flag=True
 while(flag):
   p=input("do you want to perform any operation with the result? YES OR NO\n").lower()
   if(p=='yes'):
    operation=input("enter the operation\n")
    next_no=int(input("enter the number\n"))
    n=calculation(result,operation,next_no)
    result=n
    print(f"result is {n}")     
   else:
    flag=False
    print(f"Final result is {n}") 
    calculator()
calculator()    
    



  

         