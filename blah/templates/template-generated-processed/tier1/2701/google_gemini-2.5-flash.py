def solve():
    """Index: 2701.
    Returns: Tommy's profit from selling the tomatoes.
    """
    # L1
    crate_capacity_kg = 20 # 20 kilograms of tomatoes
    num_crates = 3 # 3 crates
    total_tomatoes_kg = crate_capacity_kg * num_crates

    # L2
    rotten_tomatoes_kg = 3 # 3 kilograms of tomatoes were rotten
    sellable_tomatoes_kg = total_tomatoes_kg - rotten_tomatoes_kg

    # L3
    price_per_kg = 6 # $6 per 1 kilogram
    earnings = sellable_tomatoes_kg * price_per_kg

    # L4
    cost_of_crates = 330 # bought for $330
    profit = earnings - cost_of_crates

    # FA
    answer = profit
    return answer