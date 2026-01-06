import random
def generate_random_numbers(n, start=1, end=100):
    """Generate n random numbers between start and end."""
    return [random.randint(start, end) for _ in range(n)]

# Example usage
if __name__ == "__main__":
    count = int(input("How many random numbers do you want? "))
    numbers = generate_random_numbers(count)
    print(f"Generated numbers: {numbers}")