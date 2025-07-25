def solve():
    """Index: 5476.
    Returns: the total money Jimmy got paid for the pizzas.
    """
    # L1
    pizzas_building = 2 # 2 pizzas in a building
    pizzas_park = 3 # 3 pizzas in the park
    total_pizzas = pizzas_building + pizzas_park

    # L2
    cost_per_pizza = 12 # Each pizza costs 12 dollars
    total_pizza_value = total_pizzas * cost_per_pizza

    # L3
    num_pizzas_with_delivery_charge = 2 # 2 pizzas in a building 2 km away
    delivery_charge_per_pizza = 2 # delivery charge is 2 extra dollars
    total_delivery_charge = num_pizzas_with_delivery_charge * delivery_charge_per_pizza

    # L4
    total_paid = total_pizza_value + total_delivery_charge

    # FA
    answer = total_paid
    return answer