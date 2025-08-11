def solve():
    """Index: 3835.
    Returns: the number of mice left after all events.
    """
    # L1
    initial_mice = 8 # He starts with 8 mice
    pups_per_mouse_first_gen = 6 # who each have 6 pups
    first_gen_pups = initial_mice * pups_per_mouse_first_gen

    # L2
    total_mice_after_first_gen = first_gen_pups + initial_mice

    # L3
    pups_per_mouse_second_gen_initial = 6 # all the mice have another 6 pups
    pups_eaten_per_mouse = 2 # each adult mouse eats 2 of their pups
    surviving_pups_per_mouse_second_gen = pups_per_mouse_second_gen_initial - pups_eaten_per_mouse

    # L4
    second_gen_pups = total_mice_after_first_gen * surviving_pups_per_mouse_second_gen

    # L5
    final_total_mice = second_gen_pups + total_mice_after_first_gen

    # FA
    answer = final_total_mice
    return answer