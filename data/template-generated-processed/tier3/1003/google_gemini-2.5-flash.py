from fractions import Fraction

def solve():
    """Index: 1003.
    Returns: the total amount Cheryl pays upon signing up for the golf tournament.
    """
    # L1
    electricity_bill_cost = 800 # which costs $800
    extra_cell_phone_cost = 400 # $400 more on her monthly cell phone expenses
    cell_phone_expenses = electricity_bill_cost + extra_cell_phone_cost

    # L2
    tournament_percentage_increase = Fraction(20, 100) # 20% more than her monthly cell phone expenses
    additional_tournament_cost = tournament_percentage_increase * cell_phone_expenses

    # L3
    total_tournament_cost = cell_phone_expenses + additional_tournament_cost

    # FA
    answer = total_tournament_cost
    return answer