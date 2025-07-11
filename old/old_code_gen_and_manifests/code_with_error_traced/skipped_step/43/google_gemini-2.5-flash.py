def solve(
        initial_collapsed_buildings: int = 4, # An earthquake caused four buildings to collapse
        collapse_multiplier: int = 2, # each following earthquake would have double the number of collapsing buildings as the previous one
        num_additional_earthquakes: int = 3 # After three more earthquakes
    ):
    """Index: 43.
    Returns: the total number of buildings that had collapsed including those from the first earthquake.
    """

    #: L1
    second_earthquake_collapsed = collapse_multiplier * initial_collapsed_buildings # eval: 8 = 2 * 4

    #: L2
    third_earthquake_collapsed = collapse_multiplier * second_earthquake_collapsed # eval: 16 = 2 * 8

    #: L3
    fourth_earthquake_collapsed = collapse_multiplier * third_earthquake_collapsed # eval: 32 = 2 * 16

    #: L4

    #: FA
    answer = num_additional_earthquakes
    return answer # eval: return 3
