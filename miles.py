import sys

def km_to_miles(km):
    return km * 0.621371


if __name__ == "__main__":
    print("Convert kilometer to miles")

    # Jenkins / CLI requires argument
    if len(sys.argv) != 2:
        print("Error:")
        print("Usage: python miles.py <kilometers>")
        sys.exit(1)

    try:
        km = float(sys.argv[1])
        miles = km_to_miles(km)
        print(f"{km} kilometers = {miles} miles")

    except ValueError:
        print("Error: Kilometer value must be a number")
        sys.exit(1)
