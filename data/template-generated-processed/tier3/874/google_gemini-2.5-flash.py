def solve():
    """Index: 874.
    Returns: the number of cents Winston has left.
    """
    # L1
    quarters_count = 14 # 14 quarters
    cents_per_quarter = 25 # WK
    total_cents_initial = quarters_count * cents_per_quarter

    # L2
    dollar_value_cents = 100 # WK
    half_dollar_divisor = 2 # half a dollar
    spent_cents = dollar_value_cents / half_dollar_divisor

    # L3
    remaining_cents = total_cents_initial - spent_cents

    # FA
    answer = remaining_cents
    return answer