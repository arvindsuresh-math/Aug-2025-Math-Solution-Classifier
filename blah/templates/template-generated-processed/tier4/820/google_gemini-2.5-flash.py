def solve():
    """Index: 820.
    Returns: the total amount James paid.
    """
    # L1
    steak_egg_cost = 16 # steak and egg meal for $16
    chicken_fried_steak_cost = 14 # chicken fried steak for $14
    total_meal_cost = steak_egg_cost + chicken_fried_steak_cost

    # L2
    num_people_paying = 2 # WK
    cost_per_person = total_meal_cost / num_people_paying

    # L3
    tip_percentage = 0.2 # They tip 20%
    tip_amount = total_meal_cost * tip_percentage

    # L4
    james_total_payment = cost_per_person + tip_amount

    # FA
    answer = james_total_payment
    return answer