def solve():
    """Index: 2590.
    Returns: the total number of glasses currently being displayed.
    """
    # L1
    tall_cupboard_capacity = 20 # His tall cupboard can hold 20 glasses
    twice_factor = 2 # twice as many
    wide_cupboard_capacity = tall_cupboard_capacity * twice_factor

    # L2
    narrow_cupboard_total_capacity = 15 # his narrow cupboard can hold 15 glasses
    number_of_shelves = 3 # divided equally among the three shelves
    glasses_per_shelf = narrow_cupboard_total_capacity / number_of_shelves

    # L3
    narrow_cupboard_actual_capacity = narrow_cupboard_total_capacity - glasses_per_shelf

    # L4
    total_displayed_glasses = tall_cupboard_capacity + wide_cupboard_capacity + narrow_cupboard_actual_capacity

    # FA
    answer = total_displayed_glasses
    return answer