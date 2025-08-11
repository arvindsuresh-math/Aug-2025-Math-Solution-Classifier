def solve():
    """Index: 4583.
    Returns: the total cost of the pizza order including tip.
    """
    # L1
    pizzas_for_son = 1 # 1 for her son
    pizzas_for_daughter = 1 # 1 for her daughter
    pizzas_for_parents = 1 # 1 to share with her husband
    total_pizzas = pizzas_for_son + pizzas_for_daughter + pizzas_for_parents

    # L2
    cost_per_pizza = 10.00 # $10.00 per pizza
    base_pizza_cost = cost_per_pizza * total_pizzas

    # L3
    num_toppings = 4 # 4 toppings
    cost_per_topping = 1.00 # $1.00 per topping
    total_topping_cost = num_toppings * cost_per_topping

    # L4
    subtotal_pizza_cost = base_pizza_cost + total_topping_cost

    # L5
    tip_amount = 5.00 # $5.00 tip
    final_order_cost = tip_amount + subtotal_pizza_cost

    # FA
    answer = final_order_cost
    return answer