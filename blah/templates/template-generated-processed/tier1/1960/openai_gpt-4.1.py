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
    oranges_for_juice = 30 # 30 pieces of oranges will be kept for making orange juice
    not_sold = rotten_oranges + oranges_for_juice

    # L3
    oranges_sold = total_oranges - not_sold

    # FA
    answer = oranges_sold
    return answer