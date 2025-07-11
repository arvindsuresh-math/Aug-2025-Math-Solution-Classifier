def solve():
    """Index: 1457.
    Returns: the total number of sacks of rice after the first and second harvest.
    """
    # L1
    initial_sacks = 20 # you can get a total of 20 sacks of rice every harvest
    increase_percent = 0.20 # yield increases by twenty percent after every harvest
    first_increase = initial_sacks * increase_percent

    # L2
    second_harvest_sacks = initial_sacks + first_increase

    # L3
    total_sacks = initial_sacks + second_harvest_sacks

    # FA
    answer = total_sacks
    return answer