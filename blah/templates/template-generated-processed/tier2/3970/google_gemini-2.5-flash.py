def solve():
    """Index: 3970.
    Returns: the total number of cans of food needed for the chili.
    """
    # L1
    beans_cans = 2 # two cans of beans
    tomato_increase_percent_num = 150 # 50% more tomatoes than beans (100% original + 50% more = 150%)
    percent_factor = 0.01 # WK
    tomatoes_cans = beans_cans * tomato_increase_percent_num * percent_factor

    # L2
    chilis_cans = 1 # a can of chilis
    total_cans_per_batch = tomatoes_cans + beans_cans + chilis_cans

    # L3
    num_batches = 4 # quadruple batch
    total_cans_needed = total_cans_per_batch * num_batches

    # FA
    answer = total_cans_needed
    return answer