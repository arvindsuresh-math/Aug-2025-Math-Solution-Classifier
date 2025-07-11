def solve(
    initial_collapses: int = 4, # An earthquake caused four buildings to collapse.
    num_following_earthquakes: int = 3 # After three more earthquakes
):
    """Index: 43.
    Returns: the total number of buildings that had collapsed after three more earthquakes, including the first earthquake.
    """
    #: L1
    collapses_second_earthquake = initial_collapses * 2

    #: L2
    collapses_third_earthquake = collapses_second_earthquake * 2

    #: L3
    collapses_fourth_earthquake = collapses_third_earthquake * 2

    #: L4
    total_collapses = initial_collapses + collapses_second_earthquake + collapses_third_earthquake + collapses_fourth_earthquake

    answer = total_collapses # FINAL ANSWER
    return answer