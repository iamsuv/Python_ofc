
num=(int(input("Enter a number :")))

def isPrime(num):
    for i in range(2,num):
        mod= num % i
        if mod==0:
            return print(num,' is not Prime')

    return print(num,' is prime')

isPrime(num)


