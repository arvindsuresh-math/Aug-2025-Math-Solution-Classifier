def solve():
    """Index: 4993.
    Returns: the total savings from the promotion.
    """
    # L1
    regular_medium_pizza_price = 18 # regular medium pizza price is $18
    promotion_medium_pizza_price = 5 # next 3 medium pizzas for $5 each
    savings_per_medium_pizza = regular_medium_pizza_price - promotion_medium_pizza_price

    # L2
    num_medium_pizzas_promotion = 3 # next 3 medium pizzas
    total_savings = num_medium_pizzas_promotion * savings_per_medium_pizza

    # FA
    answer = total_savings
    return answer