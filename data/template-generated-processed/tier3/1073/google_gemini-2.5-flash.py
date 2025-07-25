from fractions import Fraction

def solve():
    """Index: 1073.
    Returns: the total number of fish left in the sea.
    """
    # L1
    westward_fraction_caught = Fraction(3, 4) # 3/4 of the fish that swam westward
    initial_westward_fish = 1800 # 1,800 fish swim westward
    westward_fish_caught = westward_fraction_caught * initial_westward_fish

    # L2
    remaining_westward_fish = initial_westward_fish - westward_fish_caught

    # L3
    eastward_fraction_caught = Fraction(2, 5) # 2/5 of the fish that swam eastward
    initial_eastward_fish = 3200 # 3,200 swim eastward
    eastward_fish_caught = eastward_fraction_caught * initial_eastward_fish

    # L4
    remaining_eastward_fish = initial_eastward_fish - eastward_fish_caught

    # L5
    initial_north_fish = 500 # 500 swim north
    total_remaining_fish = initial_north_fish + remaining_westward_fish + remaining_eastward_fish

    # FA
    answer = total_remaining_fish
    return answer