def solve():
    """Index: 2673.
    Returns: the total amount saved by the end of the third month.
    """
    # Define initial input from the question, used in subsequent calculations.
    first_month_savings = 10 # 10 dollars the first month

    # L2
    monthly_increase = 30 # 30 more each month
    savings_month_2 = first_month_savings + monthly_increase

    # L3
    savings_month_3 = savings_month_2 + monthly_increase

    # FA
    answer = savings_month_3
    return answer