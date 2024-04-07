def print_even_numbers(limit):
    print("Even numbers up to", limit, "are:")
    for num in range(2, limit + 1, 2):
        print(num, end=" ")

def main():
    try:
        limit = int(input("Enter the upper limit to generate even numbers: "))
        if limit < 2:
            print("Please enter a limit greater than or equal to 2.")
            return
        print_even_numbers(limit)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
