# put your python code here
def multiply(*args):
    prod = 1
    if len(args) == 1:
        return args[0]
    else:
        for n in args:
            prod *= n
        return prod
