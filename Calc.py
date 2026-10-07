def add(x,y):
 return(x+y)
def sub(x,y):
 return(x-y)
def mul(x,y):
 return(x*y)
def div(x,y):
 if(y==0):
  print("Division by zero is not possible")
 else:
  return(x/y)

while true():
 ch=int(input("Enter your choice"))
 num1=float(int(input("Enter your first no")))
 num2=float(int(input("Enter your second no")))

if choice=="1":
 print("the result is add{num1,num2})
if choice=="2":
 print("the result is sub{num1,num2})
if choice=="3":
 print("the result is mul{num1,num2})
if choice=="4":
 print("the result is div{num1,num2})
else:
 print("Invalid choice")
