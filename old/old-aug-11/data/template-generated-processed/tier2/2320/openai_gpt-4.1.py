def solve():
    """Index: 2320.
    Returns: the total cost of Harry's pizza order including tip.
    """
    # L1
    toppings_per_pizza = 3 # each with 3 toppings
    topping_cost = 2 # $2 per topping
    toppings_cost_per_pizza = toppings_per_pizza * topping_cost

    # L2
    large_pizza_cost = 14 # A large pizza is 14
    total_per_pizza = large_pizza_cost + toppings_cost_per_pizza

    # L3
    num_pizzas = 2 # orders 2 large pizzas
    pizzas_cost = num_pizzas * total_per_pizza

    # L4
    tip_percent = 0.25 # 25% tip
    tip_amount = pizzas_cost * tip_percent

    # L5
    total_cost = pizzas_cost + tip_amount

    # FA
    answer = total_cost
    return answer