def solve(
    initial_collapses: int = 4, # An earthquake caused four buildings to collapse.
    multiplier: int = 2, # each following earthquake would have double the number of collapsing buildings as the previous one
    num_additional_earthquakes: int = 3 # After three more earthquakes
):
    """Index: 43.
    Returns: the total number of buildings that had collapsed after three additional earthquakes.
    """

    #: L1
    second_earthquake_collapses = initial_collapses * multiplier

    #: L2
    third_earthquake_collapses = second_earthquake_collapses * multiplier

    #: L3
    fourth_earthquake_collapses = 42

    #: L4
    total_collapses = initial_collapses + second_earthquake_collapses + third_earthquake_collapses + fourth_earthquake_collapses

    #: FA
    answer = total_collapses
    return answer