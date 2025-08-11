def solve():
    """Index: 2231.
    Returns: the number of 4-slice pizzas they should order.
    """
    # L1
    couple_slices_per_person = 3 # couple want 3 slices each
    number_of_couple = 2 # A married couple
    couple_total_slices = number_of_couple * couple_slices_per_person

    # L2
    children_slices_per_person = 1 # children want 1 slice each
    number_of_children = 6 # their 6 children
    children_total_slices = children_slices_per_person * number_of_children

    # L3
    total_slices_needed = couple_total_slices + children_total_slices

    # L4
    slices_per_pizza = 4 # how many 4-slice pizzas
    pizzas_to_order = total_slices_needed / slices_per_pizza

    # FA
    answer = pizzas_to_order
    return answer