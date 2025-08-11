from fractions import Fraction

def solve():
    """Index: 3397.
    Returns: the amount of money Leo has after debts are settled.
    """
    # L1
    total_money = 48 # Leo and Ryan together have $48
    ryan_fraction = Fraction(2, 3) # Ryan owns 2/3 of the amount
    ryan_initial_money = total_money * ryan_fraction

    # L2
    leo_initial_money = total_money - ryan_initial_money

    # L3
    ryan_owed_leo = 10 # Ryan owed him $10
    leo_money_after_ryan_payment = leo_initial_money + ryan_owed_leo

    # L4
    leo_owed_ryan = 7 # he also owed Ryan $7
    leo_final_money = leo_money_after_ryan_payment - leo_owed_ryan

    # FA
    answer = leo_final_money
    return answer