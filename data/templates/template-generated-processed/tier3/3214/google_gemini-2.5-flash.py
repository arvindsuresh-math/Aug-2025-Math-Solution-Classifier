from fractions import Fraction

def solve():
    """Index: 3214.
    Returns: the total number of chickens Carla has now.
    """
    # L1
    initial_chickens = 400 # Carla had 400 chickens
    death_percentage = Fraction(40, 100) # 40% of the chicken died
    chickens_died = death_percentage * initial_chickens

    # L2
    remaining_chickens = initial_chickens - chickens_died

    # L3
    purchase_multiplier = 10 # ten times as many chickens
    new_chickens_bought = purchase_multiplier * chickens_died

    # L4
    total_chickens_now = new_chickens_bought + remaining_chickens

    # FA
    answer = total_chickens_now
    return answer