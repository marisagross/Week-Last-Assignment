# Marisa Gross
# CIS 125
# Last week Assignment
# Collaborated with Dr. Neumann 

def gCd(x, y):
    print("x = ",x, "y = ",y)
    if y == 0:
        return x
    else:
        return gCd(y, x%y)   # return gcd
        
    
def main():
    x = 252       
    y = 105
    print("GCD of",x,",",y,"=",gCd(x,y))
    
if __name__ == "__main__":
    main()
