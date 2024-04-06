def generate_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

def main():
    try:
        limit = int(input("Enter the upper limit to generate prime numbers: "))
        if limit < 2:
            print("Please enter a limit greater than or equal to 2.")
            return
        prime_numbers = generate_primes(limit)
        print("Prime numbers up to", limit, "are:", prime_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
C:\Users\SHASHI\Documents\GitHub\desktop-tutorial