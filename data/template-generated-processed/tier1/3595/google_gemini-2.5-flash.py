def solve():
    """Index: 3595.
    Returns: the total amount of money Mr. Sergio got in that season.
    """
    # L1
    mango_production = 400 # produced 400 kg of mangoes
    orange_more_than_mango = 200 # 200 kg more than that of mangoes
    orange_production = mango_production + orange_more_than_mango

    # L2
    apple_multiplier = 2 # twice the total produce of mangoes
    apple_production = apple_multiplier * mango_production

    # L3
    total_fruit_production = apple_production + orange_production + mango_production

    # L4
    price_per_kg = 50 # sold the fruits at $50 per kg
    total_income = total_fruit_production * price_per_kg

    # FA
    answer = total_income
    return answer