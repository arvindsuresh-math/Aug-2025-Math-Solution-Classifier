def solve():
    """Index: 6710.
    Returns: the total profit Tim makes from selling necklaces.
    """
    # L1
    num_charms_per_necklace = 10 # 10 charms to make each necklace
    cost_per_charm = 15 # Each charm cost $15
    cost_per_necklace = num_charms_per_necklace * cost_per_charm

    # L2
    selling_price_per_necklace = 200 # sells the necklace for $200
    profit_per_necklace = selling_price_per_necklace - cost_per_necklace

    # L3
    num_necklaces_sold = 30 # sells 30
    total_profit = profit_per_necklace * num_necklaces_sold

    # FA
    answer = total_profit
    return answer