def solve(
        initial_buildings_collapsed: int = 4  # An earthquake caused four buildings to collapse
    ):
    """Index: 43.
    Returns: the total number of buildings collapsed after four earthquakes."""
    #: L1
    second_earthquake_buildings = initial_buildings_collapsed * 2 # eval: 8 = 4 * 2
    #: L2
    third_earthquake_buildings = second_earthquake_buildings * 2 # eval: 16 = 8 * 2
    #: L3
    fourth_earthquake_buildings = third_earthquake_buildings * 2 # eval: 32 = 16 * 2
    #: L4
    total_buildings_collapsed = ( # eval: 60 = (
    initial_buildings_collapsed + # eval: 4 +
    second_earthquake_buildings + # eval: 8 +
    third_earthquake_buildings + # eval: 16 +
    fourth_earthquake_buildings # eval: 32
    )
    answer = total_buildings_collapsed  # FINAL ANSWER # eval: 60 = 60  # FINAL ANSWER
    return answer # eval: return 60