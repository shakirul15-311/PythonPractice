def make_sum(*args):
    sum = 0
    for num in args: # Here, args is like a Tuple which is (10, 20, 30, 40)
        sum += num
    return sum
