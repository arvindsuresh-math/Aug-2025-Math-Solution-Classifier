def solve(
        sarah_tall_mirror_reflections: int = 10, # she saw her reflection 10 times
        sarah_wide_mirror_reflections: int = 5, # she saw her reflection 5 times
        ellie_tall_mirror_reflections: int = 6, # she saw her reflection 6 times
        ellie_wide_mirror_reflections: int = 3, # she saw her reflection 3 times
        tall_mirror_passes: int = 3, # passed through the room with tall mirrors 3 times each
        wide_mirror_passes: int = 5 # passed through the room with wide mirrors 5 times each
    ):
    """Index: 1647.
    Returns: the total number of times Sarah and Ellie saw their reflections.
    """
    #: L1
    sarah_total_tall_reflections = sarah_tall_mirror_reflections * tall_mirror_passes

    #: L2
    sarah_total_wide_reflections = sarah_wide_mirror_reflections * wide_mirror_passes

    #: L3
    sarah_total_reflections = sarah_total_tall_reflections + sarah_total_wide_reflections

    #: L4
    ellie_total_tall_reflections = ellie_tall_mirror_reflections * tall_mirror_passes

    #: L5
    ellie_total_wide_reflections = ellie_wide_mirror_reflections * wide_mirror_passes

    #: L6
    ellie_total_reflections = ellie_total_tall_reflections + ellie_total_wide_reflections

    #: L7
    total_reflections = sarah_total_reflections + ellie_total_reflections

    answer = total_reflections # FINAL ANSWER
    return answer