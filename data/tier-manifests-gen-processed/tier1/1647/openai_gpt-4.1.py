def solve():
    """Index: 1647.
    Returns: the total number of times Sarah and Ellie saw their reflections.
    """
    # L1
    sarah_tall_reflections = 10 # every time in tall mirrors, Sarah saw her reflection 10 times
    tall_mirror_passes = 3 # both passed through the room with tall mirrors 3 times each
    sarah_tall_total = sarah_tall_reflections * tall_mirror_passes

    # L2
    sarah_wide_reflections = 5 # every time in wide mirrors, Sarah saw her reflection 5 times
    wide_mirror_passes = 5 # both passed through the room with wide mirrors 5 times each
    sarah_wide_total = sarah_wide_reflections * wide_mirror_passes

    # L3
    sarah_total = sarah_tall_total + sarah_wide_total

    # L4
    ellie_tall_reflections = 6 # every time in tall mirrors, Ellie saw her reflection 6 times
    ellie_tall_total = ellie_tall_reflections * tall_mirror_passes

    # L5
    ellie_wide_reflections = 3 # every time in wide mirrors, Ellie saw her reflection 3 times
    ellie_wide_total = ellie_wide_reflections * wide_mirror_passes

    # L6
    ellie_total = ellie_tall_total + ellie_wide_total

    # L7
    answer = sarah_total + ellie_total
    return answer