def solve():
    """Index: 831.
    Returns: the total number of popsicle sticks they can use.
    """
    # L1
    steve_sticks = 12 # If Steve has 12 popsicle sticks
    multiplier_sid = 2 # twice as many as Steve
    sid_sticks = steve_sticks * multiplier_sid

    # L2
    multiplier_sam = 3 # thrice as many as Sid
    sam_sticks = sid_sticks * multiplier_sam

    # L3
    total_sticks = sid_sticks + sam_sticks + steve_sticks

    # FA
    answer = total_sticks
    return answer