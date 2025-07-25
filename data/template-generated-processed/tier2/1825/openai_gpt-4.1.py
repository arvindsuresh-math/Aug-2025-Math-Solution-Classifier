def solve():
    """Index: 1825.
    Returns: the amount of money Tom saved by having insurance.
    """
    # L1
    insurance_months = 24 # had pet insurance for 24 months
    insurance_cost_per_month = 20 # cost $20 per month
    total_insurance_cost = insurance_months * insurance_cost_per_month

    # L2
    procedure_cost = 5000 # procedure cost $5000
    uncovered_percent = 0.2 # insurance covers all but 20%
    out_of_pocket_procedure = procedure_cost * uncovered_percent

    # L3
    total_paid_with_insurance = out_of_pocket_procedure + total_insurance_cost

    # L4
    money_saved = procedure_cost - total_paid_with_insurance

    # FA
    answer = money_saved
    return answer