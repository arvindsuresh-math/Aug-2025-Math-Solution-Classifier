from fractions import Fraction

def solve():
    """Index: 5898.
    Returns: the number of additional bollards required to install.
    """
    # L1
    bollards_per_side = 4000 # 4000 bollards on each side of a road
    num_sides = 2 # on each side of a road
    total_bollards_required = bollards_per_side * num_sides

    # L2
    fraction_installed = Fraction(3, 4) # 3/4 of the total number of bollards
    bollards_installed = fraction_installed * total_bollards_required

    # L3
    bollards_remaining_to_install = total_bollards_required - bollards_installed

    # FA
    answer = bollards_remaining_to_install
    return answer