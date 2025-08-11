from fractions import Fraction

def solve():
    """Index: 6006.
    Returns: the total number of windows tabs remaining open.
    """
    # L1
    initial_tabs = 400 # Jose had 400 tabs opened up in his windows browser
    first_closed_fraction = Fraction(1, 4) # closed 1/4 of the tabs
    first_closed_tabs = first_closed_fraction * initial_tabs

    # L2
    tabs_after_first_closure = initial_tabs - first_closed_tabs

    # L3
    second_closed_fraction = Fraction(2, 5) # closed 2/5 of the remaining tabs
    second_closed_tabs = second_closed_fraction * tabs_after_first_closure

    # L4
    tabs_after_second_closure = tabs_after_first_closure - second_closed_tabs

    # L5
    third_closed_fraction_num = 1 # from question: "half of the remaining tabs"
    third_closed_fraction_den = 2 # from question: "half of the remaining tabs"
    third_closed_divisor = 2 # from question: "half of the remaining tabs"
    third_closed_tabs = tabs_after_second_closure / third_closed_divisor

    # L6
    final_remaining_tabs = tabs_after_second_closure - third_closed_tabs

    # FA
    answer = final_remaining_tabs
    return answer