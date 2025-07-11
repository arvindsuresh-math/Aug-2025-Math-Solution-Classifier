def solve():
    """Index: 1606.
    Returns: how many more pounds Maya can lift at her peak than when she started.
    """
    # L1
    america_initial_lift = 240 # America can lift 240 pounds
    maya_initial_fraction = 0.25 # she can only lift a fourth of what America can
    maya_initial_lift = america_initial_lift * maya_initial_fraction

    # L2
    progress_increment = 10 # she can add 10 more pounds
    maya_after_progress = maya_initial_lift + progress_increment

    # L3
    america_peak_lift = 300 # America has hit her peak lift at 300 pounds
    maya_peak_fraction = 0.5 # can lift half of what America can lift
    maya_peak_lift = america_peak_lift * maya_peak_fraction

    # L4
    maya_gain = maya_peak_lift - maya_initial_lift

    # FA
    answer = maya_gain
    return answer