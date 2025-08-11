def solve():
    """Index: 2101.
    Returns: the number of pizzas they should order.
    """
    # L1
    brenda = 1 # Brenda and nine of her friends
    friends = 9 # nine of her friends
    total_people = brenda + friends

    # L2
    slices_per_person = 2 # each person will eat 2 slices
    total_slices_needed = total_people * slices_per_person

    # L3
    slices_per_pizza = 4 # each pizza has 4 slices
    pizzas_to_order = total_slices_needed / slices_per_pizza

    # FA
    answer = pizzas_to_order
    return answer