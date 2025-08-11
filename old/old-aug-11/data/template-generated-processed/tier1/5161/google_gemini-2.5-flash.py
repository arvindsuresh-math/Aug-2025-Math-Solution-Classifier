def solve():
    """Index: 5161.
    Returns: the total value of Smaug's hoard expressed as a number of copper coins.
    """
    # L1
    gold_coins = 100 # 100 gold coins
    silver_per_gold = 3 # 3 silver coins
    gold_value_in_silver = gold_coins * silver_per_gold

    # L2
    silver_coins = 60 # 60 silver coins
    total_gold_silver_in_silver = gold_value_in_silver + silver_coins

    # L3
    copper_per_silver = 8 # 8 copper coins
    gold_silver_value_in_copper = total_gold_silver_in_silver * copper_per_silver

    # L4
    copper_coins = 33 # 33 copper coins
    total_hoard_value_in_copper = gold_silver_value_in_copper + copper_coins

    # FA
    answer = total_hoard_value_in_copper
    return answer