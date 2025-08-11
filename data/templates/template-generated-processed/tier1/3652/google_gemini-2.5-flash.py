def solve():
    """Index: 3652.
    Returns: the total cost of the bill.
    """
    # L1
    num_adults = 6 # six adults
    cost_adult_meal = 6 # each adult meal cost six dollars
    cost_adult_meals = num_adults * cost_adult_meal

    # L2
    num_children = 2 # two children
    cost_child_meal = 4 # each children's meal was $4
    cost_children_meals = num_children * cost_child_meal

    # L3
    total_people_drinks = num_adults + num_children

    # L4
    cost_soda = 2 # a soda for $2
    cost_drinks = total_people_drinks * cost_soda

    # L5
    total_bill = cost_adult_meals + cost_children_meals + cost_drinks

    # FA
    answer = total_bill
    return answer