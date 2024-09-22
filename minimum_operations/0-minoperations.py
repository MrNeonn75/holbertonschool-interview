#!/usr/bin/python3
""" Task 0: 0. Minimum Operations """


def minOperations(n):
    """
    Calculate the minimum number of operations needed to reach exactly `n`
    characters in the file using only Copy All and Paste operations.

    The function works by finding the prime factors of `n` and summing them up,
    since each factor represents a copy-paste operation sequence. If `n` can be
    factorized into smaller numbers, those factors guide the number of
    operations required.

    Args:
        n (int): The target number of 'H' characters in the file.

    Returns:
        int: The minimum number of operations to reach exactly
            `n`'H' characters.
             Returns 0 if `n` is impossible to achieve (i.e., if `n` <= 1).
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # While the current n is divisible by the divisor
        while n % divisor == 0:
            operations += divisor  # Add divisor to the count of operations
            n //= divisor  # Reduce n by the divisor
        divisor += 1  # Move to the next possible divisor

    return operations
