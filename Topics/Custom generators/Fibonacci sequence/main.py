def fibonacci(n, a=0, b=1):
    
    if n == 1:
        yield 0
    elif n == 2:
        yield 1
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2

fib = fibonacci():

for num in range(n):
    num = int(n)
