from fractions import Fraction

def solve():
    """Index: 315.
    Returns: the number of days the food will last after 100 people leave the castle.
    """
    # L2
    initial_people = 300 # 300 people
    people_leaving = 100 # 100 people leave the castle
    remaining_people = initial_people - people_leaving

    # L3
    people_fraction = Fraction(remaining_people, initial_people)

    # L4
    initial_days = 90 # 90 days
    days_passed = 30 # After 30 days
    food_days_left = initial_days - days_passed
    more_days = food_days_left / people_fraction

    # FA
    answer = more_days
    return answer