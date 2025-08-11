def solve():
    """Index: 2429.
    Returns: how much more money (in cents) Bea earned than Dawn.
    """
    # L1
    bea_price_solution_decimal = 0.25 # from solution text "$0.25"
    bea_glasses_sold = 10 # 10 glasses
    dollars_to_cents_factor = 100 # WK
    bea_total_sales_cents = bea_price_solution_decimal * bea_glasses_sold * dollars_to_cents_factor

    # L2
    dawn_price_solution_decimal = 0.28 # from solution text "$0.28"
    dawn_glasses_sold = 8 # 8 glasses
    dawn_total_sales_cents = dawn_price_solution_decimal * dawn_glasses_sold * dollars_to_cents_factor

    # L3
    # These variables are derived from previous steps to match the solution text's display format
    bea_earnings_dollars_in_solution_text = bea_total_sales_cents / dollars_to_cents_factor
    dawn_earnings_dollars_in_solution_text = dawn_total_sales_cents / dollars_to_cents_factor
    difference_in_cents = (bea_earnings_dollars_in_solution_text - dawn_earnings_dollars_in_solution_text) * dollars_to_cents_factor

    # FA
    answer = difference_in_cents
    return answer