def solve(
        initial_buildings_collapsed: int = 4  # An earthquake caused four buildings to collapse
    ):
    """Index: 43.
    Returns: the total number of buildings collapsed after four earthquakes."""

    #: L1
    second_earthquake_buildings = initial_buildings_collapsed * 2

    #: L2
    third_earthquake_buildings = second_earthquake_buildings * 2

    #: L3
    fourth_earthquake_buildings = third_earthquake_buildings * 2

    #: L4
    total_buildings_collapsed = (
    initial_buildings_collapsed +
    second_earthquake_buildings +
    third_earthquake_buildings +
    fourth_earthquake_buildings
    )

    answer = total_buildings_collapsed  # FINAL ANSWER
    return answer