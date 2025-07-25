def solve():
    """Index: 613.
    Returns: the amount John personally has to pay for the hearing aids.
    """
    # L1
    hearing_aid_cost = 2500 # They cost $2500 each
    num_hearing_aids = 2 # replace both of them
    total_cost = hearing_aid_cost * num_hearing_aids

    # L2
    insurance_coverage_percent = 0.8 # Insurance covers 80% of the cost
    insurance_coverage_amount = total_cost * insurance_coverage_percent

    # L3
    john_payment = total_cost - insurance_coverage_amount

    # FA
    answer = john_payment
    return answer