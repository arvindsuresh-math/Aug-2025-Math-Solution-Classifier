from fractions import Fraction

def solve():
    """Index: 2130.
    Returns: the amount of money Amelia has left after buying all meals.
    """
    # L1
    first_course_cost = 15 # The first course costs $15
    additional_second_course_cost = 5 # the second course $5 more
    second_course_cost = first_course_cost + additional_second_course_cost

    # L2
    dessert_percentage = Fraction(25, 100) # The cost of the dessert is 25% of the price of the second course
    dessert_cost = dessert_percentage * second_course_cost

    # L3
    initial_money = 60 # Amelia has $60 to spend
    money_left = initial_money - first_course_cost - second_course_cost - dessert_cost

    # FA
    answer = money_left
    return answer