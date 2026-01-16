import sys

def km_to_miles(n):
    return n* 0.671


if __name__ == "__main__":
    print("Convert kilometer to miles")
    
    if len(sys.argv) != 2:
        print("Error:")
        print("Usage: python miles.py <kilometers>")
        sys.exit(1)

    try:
        n= float(sys.argv[1])
        converted_value= km_to_miles(n)
        print(f"{n} ") 
        print(f"{converted_value} ")

    except ValueError:
        print("invalid input")
        sys.exit(1)
