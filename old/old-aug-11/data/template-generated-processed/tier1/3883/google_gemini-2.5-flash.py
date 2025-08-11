def solve():
    """Index: 3883.
    Returns: the number of bottles Donald drinks per day.
    """
    # L1
    paul_drinks_per_day = 3 # Paul drinks 3 bottles of juice per day
    multiplier_twice = 2 # twice the number
    twice_paul_drinks = paul_drinks_per_day * multiplier_twice

    # L2
    donald_more_than_twice = 3 # 3 more than twice the number
    donald_drinks_per_day = twice_paul_drinks + donald_more_than_twice

    # FA
    answer = donald_drinks_per_day
    return answer