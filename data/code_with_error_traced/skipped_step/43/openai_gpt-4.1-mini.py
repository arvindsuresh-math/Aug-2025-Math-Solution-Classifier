def solve(
    initial_collapsed: int = 4,  # four buildings collapsed in the first earthquake
    num_following_earthquakes: int = 3  # three more earthquakes after the first
):
    """Index: 43.
    Returns: the total number of buildings collapsed after the first and three more earthquakes.
    """

    #: L1
    second_earthquake_collapsed = 2 * initial_collapsed # eval: 8 = 2 * 4

    #: L2
    third_earthquake_collapsed = 2 * second_earthquake_collapsed # eval: 16 = 2 * 8

    #: L3
    fourth_earthquake_collapsed = 2 * third_earthquake_collapsed # eval: 32 = 2 * 16

    #: L4

    #: FA
    answer = num_following_earthquakes
    return answer # eval: return 3
