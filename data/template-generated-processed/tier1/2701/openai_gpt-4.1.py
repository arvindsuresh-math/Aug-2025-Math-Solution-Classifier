def solve():
    """Index: 2701.
    Returns: Tommy's profit from selling the tomatoes.
    """
    # L1
    crate_capacity_kg = 20 # A crate can hold 20 kilograms of tomatoes
    num_crates = 3 # Tommy has 3 crates
    total_kg = crate_capacity_kg * num_crates

    # L2
    rotten_kg = 3 # 3 kilograms of tomatoes were rotten
    sellable_kg = total_kg - rotten_kg

    # L3
    price_per_kg = 6 # sell the tomatoes for $6 per 1 kilogram
    earnings = sellable_kg * price_per_kg

    # L4
    total_cost = 330 # bought for $330
    profit = earnings - total_cost

    # FA
    answer = profit
    return answer