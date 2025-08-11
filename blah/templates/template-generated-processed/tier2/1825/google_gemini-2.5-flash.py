def solve():
    """Index: 1825.
    Returns: the amount of money saved by having insurance.
    """
    # L1
    insurance_duration_months = 24 # for 24 months
    monthly_cost = 20 # cost $20 per month
    total_insurance_cost = insurance_duration_months * monthly_cost

    # L2
    procedure_cost = 5000 # procedure cost $5000
    uncovered_percent = 0.2 # all but 20% of this
    cost_with_insurance = procedure_cost * uncovered_percent

    # L3
    total_paid = cost_with_insurance + total_insurance_cost

    # L4
    money_saved = procedure_cost - total_paid

    # FA
    answer = money_saved
    return answer