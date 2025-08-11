def solve():
    """Index: 2883.
    Returns: the number of slices each person ate.
    """
    # L1
    num_pizzas = 3 # ordered 3 pizzas
    slices_per_pizza = 8 # Each pizza had 8 slices
    total_slices = num_pizzas * slices_per_pizza

    # L2
    num_people = 6 # John with his five friends
    slices_per_person = total_slices / num_people

    # FA
    answer = slices_per_person
    return answer