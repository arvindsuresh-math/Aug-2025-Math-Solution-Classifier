from fractions import Fraction

def solve():
    """Index: 1911.
    Returns: the total number of balloons they will have.
    """
    # L1
    brooke_current_balloons = 12 # his current 12
    brooke_added_balloons = 8 # adds eight balloons
    brooke_total_balloons = brooke_current_balloons + brooke_added_balloons

    # L2
    tracy_added_balloons = 24 # adds 24
    tracy_current_balloons = 6 # her current 6
    tracy_total_balloons_before_pop = tracy_added_balloons + tracy_current_balloons

    # L3
    pop_fraction = Fraction(1, 2) # pops half of her balloons
    tracy_balloons_after_pop = pop_fraction * tracy_total_balloons_before_pop

    # L4
    combined_total_balloons = tracy_balloons_after_pop + brooke_total_balloons

    # FA
    answer = combined_total_balloons
    return answer