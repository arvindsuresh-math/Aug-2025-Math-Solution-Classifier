def solve():
    """Index: 7236.
    Returns: the total number of boys and girls left.
    """
    # L1
    initial_boys = 14 # 14 boys
    boys_drop_out = 4 # 4 boys drop out
    boys_left = initial_boys - boys_drop_out

    # L2
    initial_girls = 10 # 10 girls
    girls_drop_out = 3 # 3 girls drop out
    girls_left = initial_girls - girls_drop_out

    # L3
    total_left = boys_left + girls_left

    # FA
    answer = total_left
    return answer