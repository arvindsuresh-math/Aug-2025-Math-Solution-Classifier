def solve():
    """Index: 7073.
    Returns: Leila's original savings.
    """
    # L1
    fraction_spent_on_makeup = 3/4 # 3/4 of her savings on make-up
    total_fraction = 1 # WK
    fraction_spent_on_sweater = total_fraction - fraction_spent_on_makeup

    # L4
    sweater_cost = 20 # sweater cost her $20
    reciprocal_of_sweater_fraction = 1 / fraction_spent_on_sweater
    original_savings = sweater_cost * reciprocal_of_sweater_fraction

    # FA
    answer = original_savings
    return answer