import sys
def km_to_miles(n):
    return n * 0.671

if __name__=="__main__":
    print("convert kilometer to miles")
try:
    if len (sys.argv)==2:
        n=float(input(sys.argv[1]))
    else:
        n=float(input("enter a value"))
        converted_value=km_to_miles(n)
        print(f"{n}")
        print(f"{converted_value}")
except ValueError:
    print ("invalid input")
        
        