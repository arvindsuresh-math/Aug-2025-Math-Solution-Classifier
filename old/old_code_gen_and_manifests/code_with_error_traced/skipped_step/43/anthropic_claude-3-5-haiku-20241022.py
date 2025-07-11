def solve(
        initial_buildings_collapsed: int = 4  # An earthquake caused four buildings to collapse
    ):
    """Index: 43.
    Returns: the total number of buildings collapsed after four earthquakes."""

    #: L1
    second_earthquake_buildings = initial_buildings_collapsed * 2 # eval: 8 = 4 * 2

    #: L2

    #: L3
    fourth_earthquake_buildings = initial_buildings_collapsed * 2 # eval: 8 = 4 * 2

    #: L4
    total_buildings_collapsed = ( # eval: 24 = (
    initial_buildings_collapsed + # eval: 4 +
    second_earthquake_buildings + # eval: 8 +
    initial_buildings_collapsed + # eval: 4 +
    fourth_earthquake_buildings # eval: 8
    )

    #: FA
    answer = total_buildings_collapsed
    return answer # eval: return 24
