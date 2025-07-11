def solve():
    """Index: 39.
    Returns: the difference in the number of pieces of candy Anna gets compared to Billy.
    """
    # L1
    anna_candy_per_house = 14 # 14 pieces of candy per house
    anna_num_houses = 60 # first subdivision has 60 houses
    anna_total_candy = anna_candy_per_house * anna_num_houses

    # L2
    billy_candy_per_house = 11 # 11 pieces of candy per house
    billy_num_houses = 75 # second subdivision has 75 houses
    billy_total_candy = billy_candy_per_house * billy_num_houses

    # L3
    difference_in_candy = anna_total_candy - billy_total_candy

    # FA
    answer = difference_in_candy
    return answer