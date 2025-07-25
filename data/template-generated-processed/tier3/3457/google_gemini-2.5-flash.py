def solve():
    """Index: 3457.
    Returns: the total number of coins in each chest.
    """
    # L1
    total_gold_coins = 3500 # He has 3500 gold coins
    num_chests = 5 # across 5 chests
    gold_coins_per_chest = total_gold_coins / num_chests

    # L2
    total_silver_coins = 500 # 500 silver coins
    silver_coins_per_chest = total_silver_coins / num_chests

    # L3
    bronze_multiplier = 2 # twice as many bronze coins as silver
    total_bronze_coins = bronze_multiplier * total_silver_coins

    # L4
    bronze_coins_per_chest = total_bronze_coins / num_chests

    # L5
    total_coins_per_chest = gold_coins_per_chest + silver_coins_per_chest + bronze_coins_per_chest

    # FA
    answer = total_coins_per_chest
    return answer