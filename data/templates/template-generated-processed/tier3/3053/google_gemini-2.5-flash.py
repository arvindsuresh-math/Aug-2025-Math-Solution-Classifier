def solve():
    """Index: 3053.
    Returns: the amount of money Carl's dad gave him.
    """
    # L1
    weekly_savings = 25 # saved $25 each week
    num_weeks_saved = 6 # for 6 weeks
    total_savings_initial = weekly_savings * num_weeks_saved

    # L2
    fraction_paid_bills_denominator = 3 # a third of his saving
    amount_paid_bills = total_savings_initial / fraction_paid_bills_denominator

    # L3
    savings_after_bills = total_savings_initial - amount_paid_bills

    # L4
    coat_cost = 170 # If the coat cost $170
    money_from_dad = coat_cost - savings_after_bills

    # FA
    answer = money_from_dad
    return answer