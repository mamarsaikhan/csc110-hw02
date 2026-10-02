# Name: Marla Amarsaikhan

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Asks the user for two numbers and returns both as integers."""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x = int(input("give me x: ")) # begins with a string and casts a number
    y = int(input("give me y: "))
    return x,y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Prints a*b and a+b, and returns (a*b) divided by (a+b)."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    mult_result = a*b
    print(f"mult result: {mult_result}") # f replaces {mult_result} with the number stored in that variable
    add_result = a+b
    print(f"add result: {add_result}") # {} gives a place for python to drop in a value; whatever is inside is treated as a code
    return mult_result/add_result # gives the first variable divided by the second

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Reads two integers, computes their multadd, and prints the results."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print("*" * 16)
    print("RESULTS:")
    print(f"first number: {a}")
    print(f"second number: {b}")
    print(f"multadd result: {ab_multadd}")
    print("=" * 16)

def main ():
    """Reads two integers, computes their multadd, and prints the results."""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    # TODO: add your call instead of this line
    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    
    xy_multadd = compute_multadd(x,y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)

    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
