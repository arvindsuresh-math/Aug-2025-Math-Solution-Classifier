def solve():
    """Index: 4019.
    Returns: the savings per egg in cents.
    """
    # L1
    tray_price_dollars = 12 # The price of a tray of eggs that contains 30 eggs is $12
    eggs_per_tray = 30 # a tray of eggs that contains 30 eggs
    price_per_egg_tray_dollars = tray_price_dollars / eggs_per_tray

    # L2
    cents_per_dollar = 100 # WK
    price_per_egg_tray_cents = price_per_egg_tray_dollars * cents_per_dollar

    # L3
    individual_egg_price_cents = 50 # The price per organic egg is 50 cents
    savings_per_egg_cents = individual_egg_price_cents - price_per_egg_tray_cents

    # FA
    answer = savings_per_egg_cents
    return answer