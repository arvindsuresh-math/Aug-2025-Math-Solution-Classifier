def solve():
    """Index: 4612.
    Returns: the number of eggs Samantha will have left after recovering her capital.
    """
    # L1
    dollars_capital = 5 # $5
    cents_per_dollar = 100 # 100 cents in each $1
    total_cents_capital = dollars_capital * cents_per_dollar

    # L2
    selling_price_per_egg_cents = 20 # 20 cents
    eggs_to_sell_to_recover_capital = total_cents_capital / selling_price_per_egg_cents

    # L3
    initial_eggs = 30 # 30 eggs
    eggs_left = initial_eggs - eggs_to_sell_to_recover_capital

    # FA
    answer = eggs_left
    return answer