def solve():
    """Index: 655.
    Returns: the amount of money Hawkeye was left with.
    """
    # L1
    cost_per_charge = 3.5 # $3.5 per charge
    num_charges = 4 # four times
    total_expense = num_charges * cost_per_charge

    # L2
    initial_budget = 20 # battery charging budget was $20
    remaining_balance = initial_budget - total_expense

    # FA
    answer = remaining_balance
    return answer