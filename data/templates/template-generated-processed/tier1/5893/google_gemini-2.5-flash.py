def solve():
    """Index: 5893.
    Returns: the total number of balloons inflated.
    """
    # L1
    mary_rate = 10 # Mary inflates 10 balloons per minute
    total_time = 30 # they only have 30 minutes
    mary_total_balloons = mary_rate * total_time

    # L2
    jess_rate = 7 # Jess inflates 7 balloons per minute
    jess_total_balloons = jess_rate * total_time

    # L3
    christina_rate = 4 # inflating 4 balloons per minute
    christina_late_time = 15 # Christina came 15 minutes late
    christina_total_balloons = christina_rate * christina_late_time

    # L4
    total_balloons = mary_total_balloons + jess_total_balloons + christina_total_balloons

    # FA
    answer = total_balloons
    return answer