def solve():
    """Index: 7112.
    Returns: the percentage off Asia got at the sale.
    """
    # L1
    original_price = 350 # originally priced at $350
    sale_price = 140 # bought a homecoming dress on sale for $140
    amount_saved = original_price - sale_price

    # L2
    percent_multiplier = 100 # WK
    percentage_off_decimal = amount_saved / original_price
    percentage_off_percent = percentage_off_decimal * percent_multiplier

    # FA
    answer = percentage_off_percent
    return answer