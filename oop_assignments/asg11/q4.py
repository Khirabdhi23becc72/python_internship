def count_primes(n):
    if n < 2:
        return 0

    # Initialize a list to track prime numbers
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Count the number of primes
    return sum(is_prime)

# Example usage:
n = 10
print(count_primes(n))  # Output: 4 (primes are 2, 3, 5, 7)
