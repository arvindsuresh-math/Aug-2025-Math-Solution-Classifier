from fractions import Fraction

def solve():
    """Index: 785.
    Returns: the number of people who did not buy coffee.
    """
    # L1
    coffee_fraction = Fraction(3, 5) # 3/5 of that number came to buy coffee
    total_people_served = 25 # 25 people food and drinks
    people_who_bought_coffee = coffee_fraction * total_people_served

    # L2
    people_who_did_not_buy_coffee = total_people_served - people_who_bought_coffee

    # FA
    answer = people_who_did_not_buy_coffee
    return answer