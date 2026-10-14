def simple_intrest(principal, intrest, time):
    return(principal*intrest*time)/100

if __name__=="__main__":
    p=int(input("Enter principal amount"))
    i=int(input("Enter interest"))
    t=int(input("Enter time in months"))

    print("Simple interest is:",simple_intrest(p,i,t))