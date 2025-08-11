def solve():
    """Index: 6184.
    Returns: the number of pizza slices Mrs. Kaplan has.
    """
    # L1
    pizzas_bobby_has = 2 # Bobby has 2 pizzas
    slices_per_pizza = 6 # each pizza has 6 slices
    bobby_pizza_slices = pizzas_bobby_has * slices_per_pizza

    # L2
    kaplan_fraction_denominator = 4 # 1/4 as many pizza slices
    kaplan_pizza_slices = bobby_pizza_slices / kaplan_fraction_denominator

    # FA
    answer = kaplan_pizza_slices
    return answer