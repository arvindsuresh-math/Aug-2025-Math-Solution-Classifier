def solve():
    """Index: 43.
    Returns: the total number of buildings collapsed after four earthquakes.
    """
    # L1
    first_eq_buildings = 4 # four buildings to collapse
    multiplier = 2 # double the number of collapsing buildings
    second_eq_buildings = multiplier * first_eq_buildings

    # L2
    third_eq_buildings = multiplier * second_eq_buildings

    # L3
    fourth_eq_buildings = third_eq_buildings * multiplier

    # L4
    total_collapsed = first_eq_buildings + second_eq_buildings + third_eq_buildings + fourth_eq_buildings

    # FA
    answer = total_collapsed
    return answer