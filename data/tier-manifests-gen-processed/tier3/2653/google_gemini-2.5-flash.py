def solve():
    """Index: 2653.
    Returns: the amount Mary and her two friends should pay each for the chicken.
    """
    # L1
    beef_cost_per_pound = 4 # 3 pounds of beef that cost $4 per pound
    beef_pounds = 3 # 3 pounds of beef
    total_beef_cost = beef_cost_per_pound * beef_pounds

    # L2
    oil_cost = 1 # a liter of oil that costs $1
    total_beef_and_oil_cost = total_beef_cost + oil_cost

    # L3
    total_grocery_paid = 16 # Mary's mother paid a total of $16 for the grocery
    chicken_cost = total_grocery_paid - total_beef_and_oil_cost

    # L4
    mary_count = 1 # Mary and her two friends
    friends_count = 2 # her two friends
    number_of_people = mary_count + friends_count

    # L5
    cost_per_person = chicken_cost / number_of_people

    # FA
    answer = cost_per_person
    return answer