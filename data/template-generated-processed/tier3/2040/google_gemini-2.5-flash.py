def solve():
    """Index: 2040.
    Returns: the number of pieces of pizza left per person.
    """
    # L1
    large_pizza_slices = 14 # The large has 14 slices
    small_pizza_slices = 8 # The small pizza has 8 slices
    total_slices = large_pizza_slices + small_pizza_slices

    # L2
    slices_eaten_per_person = 9 # They have both eaten 9 slices already
    total_eaten_slices = slices_eaten_per_person + slices_eaten_per_person

    # L3
    remaining_slices = total_slices - total_eaten_slices

    # L4
    number_of_people = 2 # Phil and Andre
    pieces_per_person = remaining_slices / number_of_people

    # FA
    answer = pieces_per_person
    return answer