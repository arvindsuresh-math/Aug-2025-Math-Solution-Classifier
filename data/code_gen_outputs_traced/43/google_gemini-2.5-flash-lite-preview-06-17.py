def solve(
    initial_collapses: int = 4, # An earthquake caused four buildings to collapse.
    multiplier: int = 2, # each following earthquake would have double the number of collapsing buildings as the previous one
    num_additional_earthquakes: int = 3 # After three more earthquakes
):
    """Index: 43.
    Returns: the total number of buildings that had collapsed after three additional earthquakes.
    """

    #: L1
    second_earthquake_collapses = initial_collapses * multiplier # eval: 8 = 4 * 2

    #: L2
    third_earthquake_collapses = second_earthquake_collapses * multiplier # eval: 16 = 8 * 2

    #: L3
    fourth_earthquake_collapses = third_earthquake_collapses * multiplier # eval: 32 = 16 * 2

    #: L4
    total_collapses = initial_collapses + second_earthquake_collapses + third_earthquake_collapses + fourth_earthquake_collapses # eval: 60 = 4 + 8 + 16 + 32

    #: FA
    answer = total_collapses # eval: 60 = 60
    return answer # eval: return 60
