def solve():
    """Index: 3600.
    Returns: the length of Jane's stick in inches.
    """
    # L1
    pat_stick_length = 30 # Pat's stick is 30 inches long
    dirt_covered_length = 7 # covers 7 inches of the stick in dirt
    pat_uncovered_length = pat_stick_length - dirt_covered_length

    # L2
    multiplier_half = 2 # half as long as Sarah’s stick (implies Sarah's is twice as long)
    sarah_stick_length = pat_uncovered_length * multiplier_half

    # L3
    feet_shorter = 2 # two feet shorter
    inches_per_foot = 12 # WK
    shorter_in_inches = inches_per_foot * feet_shorter

    # L4
    jane_stick_length = sarah_stick_length - shorter_in_inches

    # FA
    answer = jane_stick_length
    return answer