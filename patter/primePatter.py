

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    print()
    return primes
    

def print_prime_pattern(n):
    primes = generate_primes(n - 2)  # Adjust to account for the inclusion of 1
    print(primes)
    sequence = [1]  # Start with 1
    for i in range(len(primes) + 1):
        print("".join(map(str, sequence)))
        if i < len(primes):
            sequence.append(primes[i])

# Print the pattern with the first 5 numbers including 1
print_prime_pattern(5)
