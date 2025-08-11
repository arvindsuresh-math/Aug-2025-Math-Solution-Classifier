def solve():
    """Index: 160.
    Returns: the total amount John spent.
    """
    # L1
    other_people_splitting_cost = 3 # splits the cost with 3 other people
    john_himself = 1 # John is one of the people splitting the cost
    total_people_splitting_cost = other_people_splitting_cost + john_himself

    # L2
    burger_pounds = 100 # 100 pounds of burgers
    cost_per_pound_burger = 3 # $3 per pound
    total_burger_cost = burger_pounds * cost_per_pound_burger

    # L3
    condiments_propane_cost = 80 # $80 of condiments and propane
    total_shared_cost = total_burger_cost + condiments_propane_cost

    # L4
    cost_per_person = total_shared_cost / total_people_splitting_cost

    # L5
    alcohol_cost = 200 # alcohol which costs $200
    johns_total_spend = alcohol_cost + cost_per_person

    # FA
    answer = johns_total_spend
    return answer