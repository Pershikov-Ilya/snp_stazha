def multiply_numbers(inputs=None):
    if not inputs:
        return None

    if isinstance(inputs, str) or isinstance(inputs, float):
        x = 1
        num = str(inputs)
        z = ''.join(filter(str.isdigit, num))
        for i in z:
            z = int(i)
            x *= z
        return x if z else None

    if isinstance(inputs, list):
        x = 1
        for i in inputs:
            x *= i
        return x


print(multiply_numbers("12п3"))
