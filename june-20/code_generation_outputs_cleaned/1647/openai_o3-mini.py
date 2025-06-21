def solve(
    sarah_tall: int = 10,  # "Sarah says that every time they were in the room with tall mirrors, she saw her reflection 10 times."
    sarah_wide: int = 5,   # "and every time they were in the room with wide mirrors, she saw her reflection 5 times."
    ellie_tall: int = 6,   # "Ellie says that every time they were in the room with tall mirrors, she saw her reflection 6 times."
    ellie_wide: int = 3,   # "and every time they were in the room with wide mirrors she saw her reflection 3 times."
    tall_passes: int = 3,  # "They both passed through the room with tall mirrors 3 times each."
    wide_passes: int = 5   # "and they both passed through the room with wide mirrors 5 times each."
):
    """Index: 1647.
    Returns: the total number of times Sarah and Ellie saw their reflections.
    """
    #: L1
    sarah_tall_total = sarah_tall * tall_passes

    #: L2
    sarah_wide_total = sarah_wide * wide_passes

    #: L3
    sarah_total = sarah_tall_total + sarah_wide_total

    #: L4
    ellie_tall_total = ellie_tall * tall_passes

    #: L5
    ellie_wide_total = ellie_wide * wide_passes

    #: L6
    ellie_total = ellie_tall_total + ellie_wide_total

    #: L7
    total_reflections = sarah_total + ellie_total

    answer = total_reflections  # FINAL ANSWER
    return answer