def fibonacci(n):
    print('Hello user')
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

