def solve():
    """Index: 43.
    Returns: the total number of buildings collapsed after all earthquakes.
    """
    # L1
    initial_collapsed_buildings = 4 # four buildings to collapse
    double_factor = 2 # double the number
    second_earthquake_collapsed = double_factor * initial_collapsed_buildings

    # L2
    third_earthquake_collapsed = double_factor * second_earthquake_collapsed

    # L3
    fourth_earthquake_collapsed = third_earthquake_collapsed * double_factor

    # L4
    total_collapsed_buildings = initial_collapsed_buildings + second_earthquake_collapsed + third_earthquake_collapsed + fourth_earthquake_collapsed

    # FA
    answer = total_collapsed_buildings
    return answer