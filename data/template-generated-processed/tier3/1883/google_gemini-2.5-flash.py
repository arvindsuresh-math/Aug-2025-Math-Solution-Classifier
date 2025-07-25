def solve():
    """Index: 1883.
    Returns: the amount of gold found per hour.
    """
    # L1
    main_chest_coins = 100 # treasure chest with 100 gold coins
    half_divisor = 2 # half as much gold
    coins_per_small_bag = main_chest_coins / half_divisor

    # L2
    num_small_bags = 2 # 2 smaller bags
    total_small_bag_coins = coins_per_small_bag * num_small_bags

    # L3
    total_gold_found = main_chest_coins + total_small_bag_coins

    # L4
    diving_hours = 8 # 8 hours scuba diving
    gold_per_hour = total_gold_found / diving_hours

    # FA
    answer = gold_per_hour
    return answer