def solve():
    """Index: 3945.
    Returns: the number of nights Nelly needs to babysit to afford the pizza.
    """
    # L1
    nelly_and_friends = 15 # herself and her 14 friends
    people_per_pizza = 3 # can feed 3 people
    num_pizzas = nelly_and_friends / people_per_pizza

    # L2
    cost_per_pizza = 12 # Each pizza costs $12
    total_cost_pizzas = num_pizzas * cost_per_pizza

    # L3
    earnings_per_night = 4 # earns $4 a night
    nights_to_babysit = total_cost_pizzas / earnings_per_night

    # FA
    answer = nights_to_babysit
    return answer