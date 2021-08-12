n = int(input())

def even(x):
    yield x * 2
    
for number in range(n):
    print(next(even(number)))




# Don't forget to print out the first n numbers one by one here
