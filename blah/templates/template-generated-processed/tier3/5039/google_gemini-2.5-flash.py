def solve():
    """Index: 5039.
    Returns: the number of large pizzas sold.
    """
    # L1
    num_small_pizzas = 8 # sold 8 small pizzas
    price_small_pizza = 2 # small pizzas for $2
    earned_from_small_pizzas = num_small_pizzas * price_small_pizza

    # L2
    total_sales = 40 # sold $40 in pizzas
    earned_from_large_pizzas = total_sales - earned_from_small_pizzas

    # L3
    price_large_pizza = 8 # large pizzas for $8
    num_large_pizzas = earned_from_large_pizzas / price_large_pizza

    # FA
    answer = num_large_pizzas
    return answer