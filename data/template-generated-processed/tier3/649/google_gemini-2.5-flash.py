def solve():
    """Index: 649.
    Returns: the total cost in dollars the students will spend.
    """
    # L1
    tolu_pencils = 3 # Tolu wants 3 pencils
    melissa_pencils = 2 # Melissa wants 2 pencils
    robert_pencils = 5 # Robert wants 5 pencils
    total_pencils = tolu_pencils + melissa_pencils + robert_pencils

    # L2
    pencil_cost_cents = 20 # The price of one pencil is 20 cents
    total_cost_cents = pencil_cost_cents * total_pencils

    # L3
    cents_per_dollar = 100 # WK
    total_cost_dollars = total_cost_cents / cents_per_dollar

    # FA
    answer = total_cost_dollars
    return answer