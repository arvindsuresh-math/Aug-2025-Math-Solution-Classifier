def solve():
    """Index: 1048.
    Returns: the number of barrels left for the fourth neighborhood.
    """
    # L1
    first_neighborhood = 150 # one neighborhood uses 150 barrels of water in a week
    second_neighborhood_multiplier = 2 # twice as many barrels of water as the first neighborhood
    second_neighborhood = first_neighborhood * second_neighborhood_multiplier

    # L2
    third_neighborhood_increment = 100 # one hundred more barrels of water than the second neighborhood
    third_neighborhood = second_neighborhood + third_neighborhood_increment

    # L3
    total_first_three = first_neighborhood + second_neighborhood + third_neighborhood

    # L4
    total_barrels = 1200 # holds 1200 barrels of water
    fourth_neighborhood = total_barrels - total_first_three

    # FA
    answer = fourth_neighborhood
    return answer