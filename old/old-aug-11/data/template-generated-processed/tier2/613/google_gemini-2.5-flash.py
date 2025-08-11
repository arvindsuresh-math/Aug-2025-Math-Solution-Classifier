def solve():
    """Index: 613.
    Returns: the amount John personally has to pay for the hearing aids.
    """
    # L1
    cost_per_aid = 2500 # They cost $2500 each
    num_aids = 2 # replace both of them
    total_cost_aids = cost_per_aid * num_aids

    # L2
    insurance_coverage_decimal = 0.8 # Insurance covers 80% of the cost
    insurance_covered_amount = total_cost_aids * insurance_coverage_decimal

    # L3
    personal_payment = total_cost_aids - insurance_covered_amount

    # FA
    answer = personal_payment
    return answer