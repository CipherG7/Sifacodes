# Function to demonstrate pass-by-value behavior with immutable types
def modify_immutable(x):
    print(f"Inside function before modification: {x}")
    x = 10
    print(f"Inside function after modification: {x}")

# Function to demonstrate pass-by-reference behavior with mutable types
def modify_mutable(lst):
    print(f"Inside function before modification: {lst}")
    lst.append(4)
    print(f"Inside function after modification: {lst}")

# Main function to test the parameter passing
def main():
    # Immutable type example (integer)
    a = 5
    print(f"Before calling modify_immutable: {a}")
    modify_immutable(a)
    print(f"After calling modify_immutable: {a}")
    
    # Mutable type example (list)
    b = [1, 2, 3]
    print(f"Before calling modify_mutable: {b}")
    modify_mutable(b)
    print(f"After calling modify_mutable: {b}")

if __name__ == "__main__":
    main()
