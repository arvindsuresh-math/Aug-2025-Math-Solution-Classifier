def solve():
    """Index: 4285.
    Returns: the total number of bags of chocolates left.
    """
    # L1
    initial_bags = 3 # bought 3 bags of chocolates
    given_away = 2 # gave the 2 bags to her brothers and sisters
    remaining_after_giving = initial_bags - given_away

    # L2
    bought_again = 3 # bought another 3 bags
    total_bags_left = remaining_after_giving + bought_again

    # FA
    answer = total_bags_left
    return answer