def solve():
    """Index: 267.
    Returns: the number of pizzas Jimmy can make to bring home with the flour left.
    """
    # L1
    minutes_per_hour = 60 # WK
    minutes_per_pizza = 10 # he takes 10 min to make each pizza
    pizzas_per_hour = minutes_per_hour / minutes_per_pizza

    # L2
    total_hours = 7 # 7 hours to do so
    total_pizzas_made = total_hours * pizzas_per_hour

    # L3
    flour_per_pizza = 0.5 # each pizza needs 0.5kg of flour
    total_flour_used = total_pizzas_made * flour_per_pizza

    # L4
    initial_flour = 22 # 22kg sack of flour
    flour_left = initial_flour - total_flour_used

    # L5
    pizzas_from_leftover = flour_left / flour_per_pizza

    # FA
    answer = pizzas_from_leftover
    return answer