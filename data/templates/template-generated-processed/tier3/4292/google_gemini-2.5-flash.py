from fractions import Fraction

def solve():
    """Index: 4292.
    Returns: the number of fish remaining after loss.
    """
    # L1
    jordan_fish = 4 # Jordan caught 4 fish
    double_factor = 2 # Perry caught double what Jordan caught
    perry_fish = double_factor * jordan_fish

    # L2
    total_initial_catch = perry_fish + jordan_fish

    # L3
    lost_fraction = Fraction(1, 4) # lost one-fourth of their total catch
    lost_fish = total_initial_catch * lost_fraction

    # L4
    remaining_fish = total_initial_catch - lost_fish

    # FA
    answer = remaining_fish
    return answer