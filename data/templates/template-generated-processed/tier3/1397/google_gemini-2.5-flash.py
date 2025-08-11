def solve():
    """Index: 1397.
    Returns: the number of bags Marly needs for the soup.
    """
    # L1
    milk_quarts = 2 # 2 quarts of milk
    chicken_stock_multiplier = 3 # three times as much chicken stock
    chicken_stock_quarts = milk_quarts * chicken_stock_multiplier

    # L2
    vegetable_quarts = 1 # 1 quart of pureed vegetables
    total_soup_quarts = chicken_stock_quarts + milk_quarts + vegetable_quarts

    # L3
    quarts_per_bag = 3 # bags that can hold 3 quarts each
    num_bags_needed = total_soup_quarts / quarts_per_bag

    # FA
    answer = num_bags_needed
    return answer