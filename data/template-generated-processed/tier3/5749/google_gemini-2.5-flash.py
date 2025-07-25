def solve():
    """Index: 5749.
    Returns: the number of slices each person will get.
    """
    # L1
    num_pizzas = 3 # order three pizzas
    slices_per_pizza = 8 # Each pizza is cut into eight slices
    total_slices = num_pizzas * slices_per_pizza

    # L2
    num_coworkers = 12 # Twelve coworkers
    slices_per_person = total_slices / num_coworkers

    # FA
    answer = slices_per_person
    return answer