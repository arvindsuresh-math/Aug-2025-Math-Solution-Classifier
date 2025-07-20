def solve():
    """Index: 6544.
    Returns: George's monthly income.
    """
    # L1
    left_money = 100 # now has $100 left
    spent_on_groceries = 20 # spent $20 from the other half on groceries
    half_income = left_money + spent_on_groceries

    # L2
    multiplier_for_full_income = 2 # WK
    monthly_income = multiplier_for_full_income * half_income

    # FA
    answer = monthly_income
    return answer