# Simple Python Program to Calculate Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main function
def main():
    # Prompt user for input
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

# Execute the main function
if __name__ == "__main__":
    main()
