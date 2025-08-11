def solve():
    """Index: 4280.
    Returns: the amount Zilla deposits into her savings account in a month.
    """
    # L1
    rent_amount = 133 # spent $133 on her rent
    rent_percentage = 7 # 7% of her monthly earnings on rent
    one_percent_value = rent_amount / rent_percentage

    # L2
    total_percentage = 100 # WK
    total_monthly_earnings = one_percent_value * total_percentage

    # L3
    other_expenses_divisor = 2 # half of it on her other monthly expenses
    other_monthly_expenses = total_monthly_earnings / other_expenses_divisor

    # L4
    total_spent = rent_amount + other_monthly_expenses

    # L5
    savings_amount = total_monthly_earnings - total_spent

    # FA
    answer = savings_amount
    return answer