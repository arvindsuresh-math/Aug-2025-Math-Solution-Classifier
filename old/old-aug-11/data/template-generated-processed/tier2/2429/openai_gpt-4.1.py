def solve():
    """Index: 2429.
    Returns: how many more cents Bea earned than Dawn.
    """
    # L1
    bea_price_dollars = 0.25 # Bea sells her lemonade at 25 cents
    bea_num_glasses = 10 # Bea sold 10 glasses
    cents_per_dollar = 100 # WK
    bea_sales_cents = bea_price_dollars * bea_num_glasses * cents_per_dollar

    # L2
    dawn_price_dollars = 0.28 # Dawn sells hers at 28 cents
    dawn_num_glasses = 8 # Dawn sold 8 glasses
    dawn_sales_cents = dawn_price_dollars * dawn_num_glasses * cents_per_dollar

    # L3
    bea_sales_dollars = bea_price_dollars * bea_num_glasses # $2.50
    dawn_sales_dollars = dawn_price_dollars * dawn_num_glasses # $2.24
    difference_cents = bea_sales_dollars * cents_per_dollar - dawn_sales_dollars * cents_per_dollar

    # FA
    answer = difference_cents
    return answer