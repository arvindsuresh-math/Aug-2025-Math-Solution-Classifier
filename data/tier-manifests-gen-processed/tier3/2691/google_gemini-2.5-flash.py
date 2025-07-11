def solve():
    """Index: 2691.
    Returns: the number of fish Kyle caught.
    """
    # L1
    total_fish_caught = 36 # Carla, Kyle, and Tasha caught 36 fish
    carla_fish = 8 # Carla caught 8
    kyle_tasha_fish = total_fish_caught - carla_fish

    # L2
    number_of_people = 2 # WK
    kyle_fish = kyle_tasha_fish / number_of_people

    # FA
    answer = kyle_fish
    return answer