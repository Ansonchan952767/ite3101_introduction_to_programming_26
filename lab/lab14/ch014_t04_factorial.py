def digit_sum(n: int) -> int:
    sum = 0
    for n in str(n):
        sum += int(n)
    return sum 