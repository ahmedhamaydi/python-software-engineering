def fibonacci(n):
    if n < 0:
        raise ValueError('n should be a non-negative integer.')

    sequence = [0,1]

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    for number in range(2,n+1):
        
        sequence.append(sequence[number-1] + sequence[number - 2])
    print(sequence)
    return max(sequence)

print(fibonacci(3))