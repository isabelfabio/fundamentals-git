def fibonacci(n): # okay this seems to work just fine, no real fixing needed
    print(f"you are printing the {n}th term of the fibonacci sequence!")
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

