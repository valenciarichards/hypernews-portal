def add(digit):
    try:
        assert total is not None
    except UnboundLocalError:
        total = 0
    total += int(digit)
    yield total

number = input()
sum = 0

for char in number:
    sum += next(add(char))
    
print(sum)
