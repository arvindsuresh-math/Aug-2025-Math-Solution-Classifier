def solve():
    """Index: 1089.
    Returns: the number of cans of sprinkles remaining.
    """
    # L1
    initial_cans = 12 # twelve cans of sprinkles
    half_divisor = 2 # Half of twelve cans
    half_cans = initial_cans / half_divisor

    # L2
    less_than_value = 3 # 3 less than half as many cans
    remaining_cans = half_cans - less_than_value

    # FA
    answer = remaining_cans
    return answer