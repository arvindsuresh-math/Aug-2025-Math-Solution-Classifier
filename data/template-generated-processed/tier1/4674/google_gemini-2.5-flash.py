def solve():
    """Index: 4674.
    Returns: Steve's height in inches after growth.
    """
    # L1
    feet_initial = 5 # 5'6"
    inches_initial = 6 # 5'6"
    inches_per_foot = 12 # WK
    height_initial_inches = feet_initial * inches_per_foot + inches_initial

    # L2
    growth_inches = 6 # grows 6 inches
    height_after_growth = height_initial_inches + growth_inches

    # FA
    answer = height_after_growth
    return answer