def solve():
    """Index: 6947.
    Returns: the total number of bugs eaten by all of them.
    """
    # L1
    gecko_eats_bugs = 12 # 12 bugs
    lizard_eats_divisor = 2 # half as many bugs
    lizard_eats_bugs = gecko_eats_bugs / lizard_eats_divisor

    # L2
    frog_eats_multiplier = 3 # 3 times as many bugs as the lizard
    frog_eats_bugs = lizard_eats_bugs * frog_eats_multiplier

    # L3
    toad_eats_multiplier = 1.50 # 50% more bugs than the frog
    toad_eats_bugs = frog_eats_bugs * toad_eats_multiplier

    # L4
    total_lizard_frog_toad_bugs = lizard_eats_bugs + frog_eats_bugs + toad_eats_bugs

    # L5
    total_bugs_eaten = gecko_eats_bugs + total_lizard_frog_toad_bugs

    # FA
    answer = total_bugs_eaten
    return answer