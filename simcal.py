#function for addtion:-
def add(x , y):
     return x+y
#function for subtraction:-
def sub(x , y):
    return x-y
#function for multiplication:-
def multiply(x ,y):
    return x*y
#function for division:-
def divide(x , y):
    return x/y

print("operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


choice = input("select the operation you need:")
    


num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
    
if choice == '1':
        print(num1, "+" , num2, "=" , add(num1,num2))
        
elif choice == '2':
        print(num1, "-" ,num2, "=" ,sub(num1,num2))
        
elif choice == '3':
        print(num1, "*" , num2, "=" ,multiply(num1,num2))
        
elif choice == '4':
        print(num1, "/" , num2, "=" , divide(num1,num2))
 
else:
  print("invaild input")
    
  print("thank you")    