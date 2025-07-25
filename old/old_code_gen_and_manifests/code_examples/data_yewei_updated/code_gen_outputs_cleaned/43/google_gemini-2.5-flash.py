def solve(
        initial_collapsed_buildings: int = 4, # An earthquake caused four buildings to collapse
        collapse_multiplier: int = 2, # each following earthquake would have double the number of collapsing buildings
        additional_earthquakes: int = 3 # After three more earthquakes
    ):
    """Index: 43.
    Returns: the total number of buildings that had collapsed including those from the first earthquake.
    """
    #: L1
    collapsed_second_earthquake = initial_collapsed_buildings * collapse_multiplier

    #: L2
    collapsed_third_earthquake = collapsed_second_earthquake * collapse_multiplier

    #: L3
    collapsed_fourth_earthquake = collapsed_third_earthquake * collapse_multiplier

    #: L4
    total_collapsed_buildings = initial_collapsed_buildings + collapsed_second_earthquake + collapsed_third_earthquake + collapsed_fourth_earthquake

    answer = total_collapsed_buildings # FINAL ANSWER
    return answer