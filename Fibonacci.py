def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Number of terms in the Fibonacci series
terms = 10
for i in range(terms):
    print(fibonacci_recursive(i))
