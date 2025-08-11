from fractions import Fraction

def solve():
    """Index: 3797.
    Returns: the cost of the milkshake.
    """
    # L1
    initial_money = 10 # Ivan had $10
    money_left = 3 # had only $3 left
    total_spent_on_cupcakes_and_milkshake = initial_money - money_left

    # L2
    cupcake_fraction = Fraction(1, 5) # spent 1/5 of it
    cost_of_cupcake = initial_money * cupcake_fraction

    # L3
    cost_of_milkshake = total_spent_on_cupcakes_and_milkshake - cost_of_cupcake

    # FA
    answer = cost_of_milkshake
    return answer