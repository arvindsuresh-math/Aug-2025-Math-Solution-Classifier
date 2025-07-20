def solve():
    """Index: 3359.
    Returns: the number of large pizzas needed.
    """
    # L1
    num_people = 3 # Ben has two brothers
    slices_per_person = 12 # each eat 12 slices of pizza
    total_slices_needed = num_people * slices_per_person

    # L2
    slices_in_small_pizza = 8 # small pizzas have 8
    remaining_slices_needed = total_slices_needed - slices_in_small_pizza

    # L3
    slices_in_large_pizza = 14 # large pizzas have 14 slices
    num_large_pizzas = remaining_slices_needed / slices_in_large_pizza

    # FA
    answer = num_large_pizzas
    return answer