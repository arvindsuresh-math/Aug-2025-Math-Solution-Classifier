def solve():
    """Index: 1556.
    Returns: the number of people who ate the pizza.
    """
    # L1
    total_slices = 16 # pizza that is cut into 16 slices
    slices_left = 4 # there are 4 slices left
    slices_eaten = total_slices - slices_left

    # L2
    slices_per_person = 2 # each of them ate 2 slices of pizza
    people_eating_pizza = slices_eaten / slices_per_person

    # FA
    answer = people_eating_pizza
    return answer