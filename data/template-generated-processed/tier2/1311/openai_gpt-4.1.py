def solve():
    """Index: 1311.
    Returns: the price of the television including 15% value-added tax.
    """
    # L1
    tv_price = 1700 # TV for $1700 excluding tax
    vat_percent_num = 15 # 15% of the value-added tax
    percent_factor = 0.01 # WK
    vat_amount = tv_price * vat_percent_num * percent_factor

    # L2
    total_price = tv_price + vat_amount

    # FA
    answer = total_price
    return answer