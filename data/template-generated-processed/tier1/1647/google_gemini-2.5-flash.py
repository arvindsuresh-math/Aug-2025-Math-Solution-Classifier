def solve():
    """Index: 1647.
    Returns: the total number of times Sarah and Ellie saw their reflections.
    """
    # L1
    sarah_tall_reflections_per_pass = 10 # Sarah saw her reflection 10 times
    tall_mirror_passes = 3 # passed through the room with tall mirrors 3 times each
    sarah_total_tall_reflections = sarah_tall_reflections_per_pass * tall_mirror_passes

    # L2
    sarah_wide_reflections_per_pass = 5 # she saw her reflection 5 times
    wide_mirror_passes = 5 # passed through the room with wide mirrors 5 times each
    sarah_total_wide_reflections = sarah_wide_reflections_per_pass * wide_mirror_passes

    # L3
    sarah_total_reflections = sarah_total_tall_reflections + sarah_total_wide_reflections

    # L4
    ellie_tall_reflections_per_pass = 6 # Ellie saw her reflection 6 times
    ellie_total_tall_reflections = ellie_tall_reflections_per_pass * tall_mirror_passes

    # L5
    ellie_wide_reflections_per_pass = 3 # she saw her reflection 3 times
    ellie_total_wide_reflections = ellie_wide_reflections_per_pass * wide_mirror_passes

    # L6
    ellie_total_reflections = ellie_total_tall_reflections + ellie_total_wide_reflections

    # L7
    total_reflections_both = sarah_total_reflections + ellie_total_reflections

    # FA
    answer = total_reflections_both
    return answer