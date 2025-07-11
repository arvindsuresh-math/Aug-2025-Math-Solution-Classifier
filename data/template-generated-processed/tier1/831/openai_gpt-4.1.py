def solve():
    """Index: 831.
    Returns: the total number of popsicle sticks Sam, Sid, and Steve can use for their Art class activity.
    """
    # L1
    steve_sticks = 12 # Steve has 12 popsicle sticks
    sid_multiplier = 2 # Sid has twice as many as Steve
    sid_sticks = steve_sticks * sid_multiplier

    # L2
    sam_multiplier = 3 # Sam has thrice as many as Sid
    sam_sticks = sid_sticks * sam_multiplier

    # L3
    total_sticks = sid_sticks + sam_sticks + steve_sticks

    # FA
    answer = total_sticks
    return answer