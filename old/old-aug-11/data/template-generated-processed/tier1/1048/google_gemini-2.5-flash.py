def solve():
    """Index: 1048.
    Returns: the number of barrels left for the fourth neighborhood.
    """
    # L1
    first_neighborhood_usage = 150 # one neighborhood uses 150 barrels of water in a week
    multiplier_twice = 2 # twice as many barrels of water as the first neighborhood
    second_neighborhood_usage = first_neighborhood_usage * multiplier_twice

    # L2
    third_neighborhood_extra = 100 # one hundred more barrels of water than the second neighborhood
    third_neighborhood_usage = second_neighborhood_usage + third_neighborhood_extra

    # L3
    total_usage_first_three_neighborhoods = first_neighborhood_usage + second_neighborhood_usage + third_neighborhood_usage

    # L4
    total_capacity = 1200 # holds 1200 barrels of water
    fourth_neighborhood_leftover = total_capacity - total_usage_first_three_neighborhoods

    # FA
    answer = fourth_neighborhood_leftover
    return answer