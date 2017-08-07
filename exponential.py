def function(x, y):
    """exponential"""
    z = x
    if y == 0:
        x = 1
    else:
        while y > 1:
            x = x * z
            y = y - 1
    return x

print(function(2, 2))


def div(x, y):
    return x / y

print(div(3.0, 5.0))

I've been here heheh
