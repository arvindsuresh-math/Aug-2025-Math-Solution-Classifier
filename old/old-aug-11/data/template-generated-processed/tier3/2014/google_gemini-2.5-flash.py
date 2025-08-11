def solve():
    """Index: 2014.
    Returns: the number of additional tanks Jennifer needs to build.
    """
    # L1
    tanks_built = 3 # She built 3 tanks
    capacity_built_tanks = 15 # will hold 15 fish each
    fish_in_built_tanks = tanks_built * capacity_built_tanks

    # L2
    total_fish_needed = 75 # house a total of 75 fish
    fish_lacking_space = total_fish_needed - fish_in_built_tanks

    # L3
    capacity_new_tanks = 10 # they will hold 10 fish each
    new_tanks_needed = fish_lacking_space / capacity_new_tanks

    # FA
    answer = new_tanks_needed
    return answer