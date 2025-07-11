def solve():
    """Index: 1606.
    Returns: the difference in pounds Maya can lift between her peak and start.
    """
    # L1
    america_initial_lift = 240 # America can lift 240 pounds
    maya_initial_fraction = 0.25 # a fourth of what America can
    maya_initial_lift = america_initial_lift * maya_initial_fraction

    # L2
    maya_progress_gain = 10 # add 10 more pounds
    maya_intermediate_lift = maya_initial_lift + maya_progress_gain

    # L3
    america_peak_lift = 300 # America has hit her peak lift at 300 pounds
    maya_peak_fraction = 0.5 # can lift half of what America can lift
    maya_peak_lift = america_peak_lift * maya_peak_fraction

    # L4
    maya_lift_increase = maya_peak_lift - maya_initial_lift

    # FA
    answer = maya_lift_increase
    return answer