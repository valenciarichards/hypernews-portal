n = int(input())


def squares(x):
    yield x ** 2
        
for number in range(n):
    print(next(squares(number + 1)))


# Don't forget to print out the first n numbers one by one here
