def factorial(n):
    # Check if n is a non-negative integer using an assertion
    assert n >= 0 and int(n) == n, "The Number must be positive"

    # Base case: If n is 0 or 1, return 1
    if n in [0, 1]:
        return 1
    else:
        # Recursive case: Calculate factorial by multiplying n with factorial of (n-1)
        return n * factorial(n - 1)

# Example usage: Calculate the factorial of 5
print(factorial(8))
