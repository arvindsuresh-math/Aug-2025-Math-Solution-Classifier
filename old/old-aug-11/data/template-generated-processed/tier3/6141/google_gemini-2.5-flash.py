from fractions import Fraction

def solve():
    """Index: 6141.
    Returns: the total amount of money Mallory used for the journey.
    """
    # L1
    total_distance = 2000 # 2000 miles away
    distance_per_tank = 500 # 500 miles before refilling
    num_refills = total_distance / distance_per_tank

    # L2
    cost_per_refill = 45 # $45
    total_fuel_cost = cost_per_refill * num_refills

    # L3
    food_cost_fraction = Fraction(3, 5) # 3/5 times as much money on food
    total_food_cost = food_cost_fraction * total_fuel_cost

    # L4
    total_expenses = total_food_cost + total_fuel_cost

    # FA
    answer = total_expenses
    return answer