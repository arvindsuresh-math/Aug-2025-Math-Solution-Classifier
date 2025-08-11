from fractions import Fraction

def solve():
    """Index: 3604.
    Returns: the amount of food remaining in the food bank.
    """
    # L1
    first_week_donations = 40 # 40 pounds of food were donated to the food bank in the first week
    multiplier = 2 # donations were twice as high as the first week
    second_week_donations = multiplier * first_week_donations

    # L2
    total_donated_food = first_week_donations + second_week_donations

    # L3
    percentage_given_out = Fraction(70, 100) # 70% of the donated food
    food_given_out = percentage_given_out * total_donated_food

    # L4
    food_remaining = total_donated_food - food_given_out

    # FA
    answer = food_remaining
    return answer