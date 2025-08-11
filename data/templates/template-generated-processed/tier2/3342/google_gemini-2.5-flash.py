def solve():
    """Index: 3342.
    Returns: the total number of pizzas Daria and Don eat altogether.
    """
    # L1
    daria_consumption_factor = 2.5 # 2.5 times the amount of pizza
    don_pizzas = 80 # Don eats 80 pizzas
    daria_pizzas = daria_consumption_factor * don_pizzas

    # L2
    total_pizzas = daria_pizzas + don_pizzas

    # FA
    answer = total_pizzas
    return answer