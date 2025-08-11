def solve():
    """Index: 1299.
    Returns: the total number of weeds Sarah pulled up.
    """
    # L1
    weeds_tuesday = 25 # On Tuesday she pulled 25 weeds
    wednesday_multiplier = 3 # three times the number of weeds
    weeds_wednesday = weeds_tuesday * wednesday_multiplier

    # L2
    thursday_divisor = 5 # one-fifth of the weeds
    weeds_thursday = weeds_wednesday / thursday_divisor

    # L3
    friday_reduction = 10 # 10 fewer weeds
    weeds_friday = weeds_thursday - friday_reduction

    # L4
    total_weeds = weeds_tuesday + weeds_wednesday + weeds_thursday + weeds_friday

    # FA
    answer = total_weeds
    return answer