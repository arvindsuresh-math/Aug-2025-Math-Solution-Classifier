def solve(
    initial_collapsed_buildings: int = 4, # An earthquake caused four buildings to collapse
    collapse_multiplier: int = 2, # each following earthquake would have double the number of collapsing buildings as the previous one
    num_additional_earthquakes: int = 3 # After three more earthquakes
):
    """Index: 43.
    Returns: the total number of buildings collapsed after the specified number of additional earthquakes, including the first one.
    """

    #: L1
    collapsed_earthquake_2 = initial_collapsed_buildings * collapse_multiplier # eval: 8 = 4 * 2

    #: L2
    collapsed_earthquake_3 = collapsed_earthquake_2 * collapse_multiplier # eval: 16 = 8 * 2

    #: L3
    collapsed_earthquake_4 = collapsed_earthquake_3 * collapse_multiplier # eval: 32 = 16 * 2

    #: L4
    total_collapsed_buildings = initial_collapsed_buildings + collapsed_earthquake_2 + collapsed_earthquake_3 + collapsed_earthquake_4 # eval: 60 = 4 + 8 + 16 + 32

    #: FA
    answer = total_collapsed_buildings
    return answer # eval: return 60
