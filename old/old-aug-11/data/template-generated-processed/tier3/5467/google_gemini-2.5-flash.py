def solve():
    """Index: 5467.
    Returns: the number of pizzas the group should order.
    """
    # L1
    num_people = 18 # group of 18 people
    slices_per_person = 3 # each person gets 3 slices
    total_slices_needed = num_people * slices_per_person

    # L2
    slices_per_pizza = 9 # each pizza has 9 slices
    num_pizzas_to_order = total_slices_needed / slices_per_pizza

    # FA
    answer = num_pizzas_to_order
    return answer