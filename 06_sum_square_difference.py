def sum_square():
    
    # find sum of squares 
    sum_square = 0

    for i in range(1, 101):
        sum_square += (i**2)

    # find square of sum
    square_sum = 0

    sum = 0
    for i in range(1, 101):
        sum += i

    square_sum = sum**2

    return (sum_square, square_sum)

print(sum_square())