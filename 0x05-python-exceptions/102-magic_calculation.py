def magic_calculation(a, b):
    """Performs a calculation based on the input values."""
    result = 0
    if a < b:
        for i in range(1, 3):  # This loops for i = 1 and i = 2
            result += (a ** i) + (b ** i)
    else:
        for i in range(1, 3):
            result += (a / i) + (b / i)
    return result
