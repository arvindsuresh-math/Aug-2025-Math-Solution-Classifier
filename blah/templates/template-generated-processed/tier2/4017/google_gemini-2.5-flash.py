def solve():
    """Index: 4017.
    Returns: Tom's out-of-pocket cost.
    """
    # L1
    visit_cost = 300 # The visit cost $300
    cast_cost = 200 # the cast cost $200
    total_cost = visit_cost + cast_cost

    # L2
    insurance_coverage_decimal = 0.6 # insurance covered 60%
    insurance_paid_amount = total_cost * insurance_coverage_decimal

    # L3
    out_of_pocket_cost = total_cost - insurance_paid_amount

    # FA
    answer = out_of_pocket_cost
    return answer