def solve():
    """Index: 1311.
    Returns: the price of the television including tax.
    """
    # L1
    tv_price_before_tax = 1700 # TV for $1700 excluding tax
    tax_rate_percent = 15 # 15% of the value-added tax
    percent_factor = 0.01 # WK
    value_added_tax = tv_price_before_tax * tax_rate_percent * percent_factor

    # L2
    total_price_with_tax = tv_price_before_tax + value_added_tax

    # FA
    answer = total_price_with_tax
    return answer