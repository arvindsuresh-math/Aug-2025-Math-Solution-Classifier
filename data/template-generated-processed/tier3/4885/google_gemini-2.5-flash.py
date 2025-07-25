from fractions import Fraction

def solve():
    """Index: 4885.
    Returns: the amount Jade saves per month.
    """
    # L1
    monthly_income = 1600 # $1600 per month
    living_expense_percentage = Fraction(75, 100) # 75% of it on living expenses
    living_expenses = monthly_income * living_expense_percentage

    # L2
    insurance_fraction = Fraction(1, 5) # one-fifth on insurance
    insurance_cost = monthly_income * insurance_fraction

    # L3
    total_expenses = living_expenses + insurance_cost

    # L4
    monthly_savings = monthly_income - total_expenses

    # FA
    answer = monthly_savings
    return answer