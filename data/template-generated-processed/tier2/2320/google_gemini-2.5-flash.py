def solve():
    """Index: 2320.
    Returns: the total cost of the pizza order including tip.
    """
    # L1
    num_toppings_per_pizza = 3 # each with 3 toppings
    cost_per_topping = 2 # $2 per topping
    cost_toppings_per_pizza = num_toppings_per_pizza * cost_per_topping

    # L2
    base_pizza_cost = 14 # A large pizza is 14
    total_cost_per_pizza = base_pizza_cost + cost_toppings_per_pizza

    # L3
    num_pizzas = 2 # He orders 2 large pizzas
    total_pizzas_cost = num_pizzas * total_cost_per_pizza

    # L4
    tip_percent = 0.25 # adds a 25% tip
    tip_amount = total_pizzas_cost * tip_percent

    # L5
    final_total_cost = total_pizzas_cost + tip_amount

    # FA
    answer = final_total_cost
    return answer