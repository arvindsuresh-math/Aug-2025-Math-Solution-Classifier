from fractions import Fraction

def solve():
    """Index: 4648.
    Returns: the amount Vince saves.
    """
    # L1
    customers_served = 80 # 80 customers a month
    earnings_per_head = 18 # $18 per head
    monthly_earnings = customers_served * earnings_per_head

    # L2
    recreation_percentage = Fraction(20, 100) # 20% of his earnings
    recreation_allocation = recreation_percentage * monthly_earnings

    # L3
    fixed_expenses = 280 # $280 for rent and electricity
    total_monthly_expenses = fixed_expenses + recreation_allocation

    # L4
    amount_saved = monthly_earnings - total_monthly_expenses

    # FA
    answer = amount_saved
    return answer