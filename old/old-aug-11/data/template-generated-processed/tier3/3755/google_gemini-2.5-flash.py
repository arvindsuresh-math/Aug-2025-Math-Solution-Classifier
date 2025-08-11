from fractions import Fraction

def solve():
    """Index: 3755.
    Returns: the number of fish the whole colony caught per day at the beginning of the first year.
    """
    # L1
    current_penguins = 1077 # The colony has 1077 penguins in it now
    gained_this_year = 129 # colony only gained 129 penguins
    penguins_before_gain_this_year = current_penguins - gained_this_year

    # L2
    tripled_factor = 3 # then tripled in the next year
    penguins_beginning_second_year = penguins_before_gain_this_year / tripled_factor

    # L3
    doubled_factor = 2 # size doubled in the first year
    penguins_beginning_first_year = penguins_beginning_second_year / doubled_factor

    # L4
    fish_per_penguin = Fraction(3, 2) # one and a half fish
    total_fish_per_day = penguins_beginning_first_year * fish_per_penguin

    # FA
    answer = total_fish_per_day
    return answer