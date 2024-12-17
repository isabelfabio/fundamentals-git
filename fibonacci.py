def fibonacci(n):
    print(f"you are printing the {n}th term of the fibonacci sequence!")
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

