def solve():
    """Index: 6507.
    Returns: the number of sheets of paper Justine used.
    """
    # L1
    total_sheets = 2450 # 2450 sheets of paper
    num_binders = 5 # 5 binders
    sheets_per_binder = total_sheets / num_binders

    # L2
    fraction_used_denominator = 2 # one-half of the sheets of paper
    sheets_justine_used = sheets_per_binder / fraction_used_denominator

    # FA
    answer = sheets_justine_used
    return answer