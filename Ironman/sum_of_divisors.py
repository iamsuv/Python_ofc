num=(int(input("Enter a number :")))

def sum_of_div(num):
    sum=0
    for i in range(2,num):
        mod=num%i
        if mod==0:
            sum=sum+i

    print('sum is :',sum)

sum_of_div(num)
