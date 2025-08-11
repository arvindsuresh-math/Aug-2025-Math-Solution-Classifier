def solve():
    """Index: 3414.
    Returns: the total money John makes per week.
    """
    # L1
    baskets_per_week = 3 # 3 crab baskets a week
    crabs_per_basket = 4 # Each basket holds 4 crabs
    crabs_per_collection_time = baskets_per_week * crabs_per_basket

    # L2
    collection_times_per_week = 2 # collects crabs twice a week
    total_crabs_per_week = crabs_per_collection_time * collection_times_per_week

    # L3
    price_per_crab = 3 # Each crab sells for $3
    money_per_week = total_crabs_per_week * price_per_crab

    # FA
    answer = money_per_week
    return answer