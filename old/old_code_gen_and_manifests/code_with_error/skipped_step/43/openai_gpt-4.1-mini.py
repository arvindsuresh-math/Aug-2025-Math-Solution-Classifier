def solve(
    initial_collapsed: int = 4,  # four buildings collapsed in the first earthquake
    num_following_earthquakes: int = 3  # three more earthquakes after the first
):
    """Index: 43.
    Returns: the total number of buildings collapsed after the first and three more earthquakes.
    """

    #: L1
    second_earthquake_collapsed = 2 * initial_collapsed

    #: L2
    third_earthquake_collapsed = 2 * second_earthquake_collapsed

    #: L3
    fourth_earthquake_collapsed = 2 * third_earthquake_collapsed

    #: L4

    #: FA
    answer = num_following_earthquakes
    return answer