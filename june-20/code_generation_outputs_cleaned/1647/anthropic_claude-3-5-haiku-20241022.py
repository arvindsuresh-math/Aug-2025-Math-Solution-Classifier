def solve(
    sarah_tall_mirror_reflections: int = 10,  # Sarah saw her reflection 10 times in tall mirrors
    sarah_wide_mirror_reflections: int = 5,   # Sarah saw her reflection 5 times in wide mirrors
    ellie_tall_mirror_reflections: int = 6,   # Ellie saw her reflection 6 times in tall mirrors
    ellie_wide_mirror_reflections: int = 3,   # Ellie saw her reflection 3 times in wide mirrors
    tall_mirror_passes: int = 3,              # They both passed through tall mirror rooms 3 times
    wide_mirror_passes: int = 5               # They both passed through wide mirror rooms 5 times
):
    """Index: 1647.
    Returns: the total number of times Sarah and Ellie saw their reflections."""
    
    #: L1
    sarah_tall_mirror_total = sarah_tall_mirror_reflections * tall_mirror_passes
    
    #: L2
    sarah_wide_mirror_total = sarah_wide_mirror_reflections * wide_mirror_passes
    
    #: L3
    sarah_total_reflections = sarah_tall_mirror_total + sarah_wide_mirror_total
    
    #: L4
    ellie_tall_mirror_total = ellie_tall_mirror_reflections * tall_mirror_passes
    
    #: L5
    ellie_wide_mirror_total = ellie_wide_mirror_reflections * wide_mirror_passes
    
    #: L6
    ellie_total_reflections = ellie_tall_mirror_total + ellie_wide_mirror_total
    
    #: L7
    answer = sarah_total_reflections + ellie_total_reflections  # FINAL ANSWER
    return answer