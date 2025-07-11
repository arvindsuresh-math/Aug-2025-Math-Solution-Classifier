def solve():
    """Index: 2458.
    Returns: the amount of Robert's monthly expenses.
    """
    # L1
    total_sales = 23600 # Last month, his total sales were $23600
    commission_percentage_numerator = 10 # 10% commission
    commission_percentage_denominator = 100 # 10% commission
    commission_earned = total_sales * commission_percentage_numerator / commission_percentage_denominator

    # L2
    basic_salary = 1250 # basic salary of $1250 per month
    total_earnings = basic_salary + commission_earned

    # L3
    savings_percentage_numerator = 20 # 20% of his total earnings to savings
    savings_percentage_denominator = 100 # 20% of his total earnings to savings
    amount_saved = total_earnings * savings_percentage_numerator / savings_percentage_denominator

    # L4
    monthly_expenses = total_earnings - amount_saved

    # FA
    answer = monthly_expenses
    return answer