def is_strange_number(n):
    digits = [int(d) for d in str(n)]
    sum_of_squares = sum(d**2 for d in digits)
    square_of_sum = (sum(digits))**2
    return sum_of_squares == square_of_sum

def count_strange_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if is_strange_number(i):
            count += 1
    return count

n = int(input())
print(count_strange_numbers(n))