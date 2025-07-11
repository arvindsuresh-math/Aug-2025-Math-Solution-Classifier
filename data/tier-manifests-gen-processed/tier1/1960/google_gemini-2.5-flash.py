def solve():
    """Index: 1960.
    Returns: the number of pieces of oranges that will be sold.
    """
    # L1
    num_bags = 10 # 10 bags
    oranges_per_bag = 30 # 30 oranges each
    total_oranges = num_bags * oranges_per_bag

    # L2
    rotten_oranges = 50 # 50 pieces of oranges are rotten
    juice_oranges = 30 # Thirty pieces of oranges will be kept for making orange juice
    not_sold_oranges = rotten_oranges + juice_oranges

    # L3
    sold_oranges = total_oranges - not_sold_oranges

    # FA
    answer = sold_oranges
    return answer