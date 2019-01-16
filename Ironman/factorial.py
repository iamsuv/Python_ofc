num=(int(input("Enter a number :")))

def factorial(num):
    product=1
    for i in range(1,num+1):
        product=product*i
    print('factorial of ',num,'is :',product)

factorial(num)