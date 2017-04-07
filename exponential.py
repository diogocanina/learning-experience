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
