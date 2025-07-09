def solve(
        initial_collapsed_buildings: int = 4, # An earthquake caused four buildings to collapse
        collapse_multiplier: int = 2, # each following earthquake would have double the number of collapsing buildings as the previous one
        num_additional_earthquakes: int = 3 # After three more earthquakes
    ):
    """Index: 43.
    Returns: the total number of buildings that had collapsed including those from the first earthquake.
    """

    #: L1
    second_earthquake_collapsed = 18 # eval: 18 = 18

    #: L2
    third_earthquake_collapsed = collapse_multiplier * second_earthquake_collapsed # eval: 36 = 2 * 18

    #: L3
    fourth_earthquake_collapsed = collapse_multiplier * third_earthquake_collapsed # eval: 72 = 2 * 36

    #: L4
    total_collapsed_buildings = initial_collapsed_buildings + second_earthquake_collapsed + third_earthquake_collapsed + fourth_earthquake_collapsed # eval: 130 = 4 + 18 + 36 + 72

    #: FA
    answer = total_collapsed_buildings
    return answer # eval: return 130
