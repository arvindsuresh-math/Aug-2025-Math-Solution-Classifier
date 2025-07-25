def solve():
    """Index: 3285.
    Returns: the number of additional toys Mohamed donated compared to Leila.
    """
    # L1
    leila_bags = 2 # 2 bags
    leila_toys_per_bag = 25 # 25 toys in each bag
    leila_total_toys = leila_bags * leila_toys_per_bag

    # L2
    mohamed_bags = 3 # 3 bags
    mohamed_toys_per_bag = 19 # 19 toys in each bag
    mohamed_total_toys = mohamed_bags * mohamed_toys_per_bag

    # L3
    difference_in_toys = mohamed_total_toys - leila_total_toys

    # FA
    answer = difference_in_toys
    return answer