def solve():
    """Index: 5490.
    Returns: the number of toys each rabbit would have.
    """
    # L1
    toys_monday = 6 # On Monday, he bought 6 toys
    wednesday_multiplier = 2 # twice as many toys as he did Monday
    toys_wednesday = toys_monday * wednesday_multiplier

    # L2
    friday_multiplier = 4 # four times as many toys as he did on Monday
    toys_friday = toys_monday * friday_multiplier

    # L3
    saturday_divisor = 2 # half as many toys as he did on Wednesday
    toys_saturday = toys_wednesday / saturday_divisor

    # L4
    total_toys = toys_monday + toys_wednesday + toys_friday + toys_saturday

    # L5
    num_rabbits = 16 # Junior has 16 rabbits
    toys_per_rabbit = total_toys / num_rabbits

    # FA
    answer = toys_per_rabbit
    return answer