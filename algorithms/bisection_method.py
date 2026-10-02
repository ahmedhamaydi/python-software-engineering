def square_root_bisection(number, tolerance=0.01, maximum_iterations=10):
    if number < 0:
        raise ValueError(
            'Square root of negative number is not defined in real numbers'
        )

    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    lower = 0
    upper = max(number, 1)  # fixed: handles 0 < number < 1
    iteration = 0

    while iteration < maximum_iterations:
        value = (lower + upper) / 2

        if value ** 2 > number:
            upper = value
        else:
            lower = value

        iteration += 1

        if upper - lower <= tolerance:
            value = (lower + upper) / 2
            print(f'The square root of {number} is approximately {value}')
            return value

    print(f'Failed to converge within {maximum_iterations} iterations')
    return None