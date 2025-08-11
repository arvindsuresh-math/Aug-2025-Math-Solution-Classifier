from fractions import Fraction

def solve():
    """Index: 315.
    Returns: the number of additional days until all the food runs out.
    """
    # L1
    initial_people = 300 # 300 people
    initial_days = 90 # 90 days
    days_passed = 30 # After 30 days
    remaining_days_for_initial_people = initial_days - days_passed

    # L2
    people_leaving = 100 # 100 people leave
    remaining_people = initial_people - people_leaving

    # L3
    consumption_ratio = Fraction(remaining_people, initial_people)

    # L4
    days_food_will_last = remaining_days_for_initial_people / consumption_ratio

    # FA
    answer = days_food_will_last
    return answer