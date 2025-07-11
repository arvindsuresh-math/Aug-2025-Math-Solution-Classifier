def solve():
    """Index: 1429.
    Returns: the selling price for each phone.
    """
    # L1
    initial_investment = 3000 # bought 200 units for just $3000
    profit_fraction_denominator = 3 # gain a third of the initial investment
    total_profit = initial_investment / profit_fraction_denominator

    # L2
    total_units = 200 # bought 200 units
    profit_per_phone = total_profit / total_units

    # L3
    cost_per_phone = initial_investment / total_units

    # L4
    selling_price_per_phone = cost_per_phone + profit_per_phone

    # FA
    answer = selling_price_per_phone
    return answer