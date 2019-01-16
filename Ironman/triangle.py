num=(int(input("Enter a number :")))

def num_triangle(num):
    for i in range(1,num+1):
        for j in range(1,i+1,+1):
            print(j,end=' ')
        print()

def star_triangle(num):
    for i in range(1,num+1):
        for j in range(1,i+1,+1):
            print("*",end=' ')
        print()

def num_triangle_rev(num):
    for i in range(num,0,-1):
        for j in range(1,i,+1):
            print(j,end=' ')
        print()

def star_triangle_rev(num):
    for i in range(num,0,-1):
        for j in range(1,i,+1):
            print("*",end=' ')
        print()

num_triangle(num)
num_triangle_rev(num)
star_triangle(num)
star_triangle_rev(num)


