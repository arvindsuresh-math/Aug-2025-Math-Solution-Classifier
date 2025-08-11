def solve():
    """Index: 1469.
    Returns: the number of marbles James has left.
    """
    # L1
    total_marbles = 28 # James has 28 marbles
    num_bags = 4 # He puts them into 4 bags
    marbles_per_bag = total_marbles / num_bags

    # L2
    marbles_remaining = total_marbles - marbles_per_bag

    # FA
    answer = marbles_remaining
    return answer