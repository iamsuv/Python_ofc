# squre upto a number
num=(int(input("Enter a number :")))

def limit(num):
    i=0
    while i*i<num:
        print(i*i)
        i+=1

limit(num)
