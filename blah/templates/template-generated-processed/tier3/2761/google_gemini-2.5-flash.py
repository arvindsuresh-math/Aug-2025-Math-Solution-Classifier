from fractions import Fraction

def solve():
    """Index: 2761.
    Returns: the total number of fish Will and Henry have altogether.
    """
    # L1
    will_catfish = 16 # Will catches 16 catfish
    will_eels = 10 # and 10 eels
    will_total_fish = will_catfish + will_eels

    # L2
    trout_per_catfish = 3 # catch 3 trout for every catfish Will catches
    henry_caught_trout = will_catfish * trout_per_catfish

    # L3
    half_fraction = Fraction(1, 2) # WK
    trout_returned = half_fraction * henry_caught_trout

    # L4
    henry_remaining_trout = henry_caught_trout - trout_returned

    # L5
    total_fish_altogether = will_total_fish + henry_remaining_trout

    # FA
    answer = total_fish_altogether
    return answer