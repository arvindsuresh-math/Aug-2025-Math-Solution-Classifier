from fractions import Fraction

def solve():
    """Index: 6002.
    Returns: the amount of money remaining after expenses.
    """
    # L1
    rent = 1200 # Her rent was $1200
    food_travel_multiplier = 2 # 1/2 of what she spent on food and travel expenses
    food_travel_expenses = rent * food_travel_multiplier

    # L2
    rent_share_fraction = Fraction(1, 2) # 1/2*1200
    rent_share_divisor = 2 # shared the rent
    shared_rent_cost = rent_share_fraction * rent

    # L3
    total_monthly_expenses = shared_rent_cost + food_travel_expenses

    # L4
    salary = 5000 # her salary was $5000 per month
    money_remaining = salary - total_monthly_expenses

    # FA
    answer = money_remaining
    return answer