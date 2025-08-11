def solve():
    """Index: 5255.
    Returns: the number of slices each person eats.
    """
    # L1
    initial_cheese_slices = 16 # They both have 16 slices
    remaining_cheese_slices = 7 # 7 slices of cheese
    eaten_cheese_slices = initial_cheese_slices - remaining_cheese_slices

    # L2
    people_eating_cheese = 3 # while the rest have an equal number of slices of each
    cheese_slices_per_person = eaten_cheese_slices / people_eating_cheese

    # L3
    types_of_slices_eaten = 2 # WK
    total_slices_per_person = cheese_slices_per_person * types_of_slices_eaten

    # FA
    answer = total_slices_per_person
    return answer