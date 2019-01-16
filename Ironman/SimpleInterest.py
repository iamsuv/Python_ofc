
def calc_simple_interest(p,t,r):
    total_interest=p+(p*r*0.01*t)
    print(total_interest)
    print(type(total_interest))

calc_simple_interest(1200,5,5)
