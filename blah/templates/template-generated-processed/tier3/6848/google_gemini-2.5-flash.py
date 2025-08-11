def solve():
    """Index: 6848.
    Returns: the total amount Olivia pays in dollars.
    """
    # L1
    quarters_for_chips = 4 # 4 quarters for chips
    quarters_per_dollar = 4 # WK
    dollars_for_chips = quarters_for_chips / quarters_per_dollar

    # L2
    quarters_for_soda = 12 # 12 quarters for soda
    dollars_for_soda = quarters_for_soda / quarters_per_dollar

    # L3
    total_dollars_paid = dollars_for_chips + dollars_for_soda

    # FA
    answer = total_dollars_paid
    return answer