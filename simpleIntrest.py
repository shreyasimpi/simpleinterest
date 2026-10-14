import sys

def simple_intrest(principal, intrest, time):
    return(principal*intrest*time)/100

if __name__=="__main__":
    p=int(sys.argv[1])
    i=float(sys.argv[2])
    t=int(sys.argv[3])

    print("Simple interest is:",simple_intrest(p,i,t))