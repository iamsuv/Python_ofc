from builtins import print

number1=int(input("Enter 1st no"))
number2=int(input("Enter 2nd no"))
print ("....MENU....")
print ("1- Add")
print ("2- Sub")
print ("3- Mul")
print ("4- Div")

choice=int(input("Choose operation ... :"))

if choice==1:
    Result=number1+number2


elif choice==2:
    Result=number1-number2


elif choice==3:
    Result=number1*number2


elif choice==4:
    Result=number1/number2


else:
    Result="Plz enter the choice from Menu"
print("Result : ",Result)