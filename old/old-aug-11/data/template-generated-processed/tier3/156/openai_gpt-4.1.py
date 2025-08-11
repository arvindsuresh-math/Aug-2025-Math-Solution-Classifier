from fractions import Fraction

def solve():
    """Index: 156.
    Returns: the total amount George paid for his food.
    """
    # L1
    sandwich_cost = 4 # The sandwich was for $4
    juice_multiplier = 2 # juice was two times more expensive
    juice_cost = sandwich_cost * juice_multiplier

    # L2
    sandwich_and_juice_total = sandwich_cost + juice_cost

    # L3
    milk_percentage = Fraction(75, 100) # 75% of the total cost of the sandwich and juice
    milk_cost = milk_percentage * sandwich_and_juice_total

    # L4
    total_cost = sandwich_and_juice_total + milk_cost

    # FA
    answer = total_cost
    return answer