def solve():
    """Index: 655.
    Returns: the amount of money Hawkeye was left with after charging his battery four times.
    """
    # L1
    num_charges = 4 # charged his battery four times
    cost_per_charge = 3.5 # $3.5 per charge
    total_expense = num_charges * cost_per_charge

    # L2
    budget = 20 # battery charging budget was $20
    balance = budget - total_expense

    # FA
    answer = balance
    return answer