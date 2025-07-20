def solve():
    """Index: 5045.
    Returns: the total number of inches of ribbon Mr. Sanchez bought.
    """
    # L1
    rope_last_week = 6 # bought 6 feet of rope
    less_this_week = 4 # bought 4 feet less than last week
    rope_this_week = rope_last_week - less_this_week

    # L2
    total_feet_rope = rope_last_week + rope_this_week

    # L3
    inches_per_foot = 12 # WK
    total_inches_rope = total_feet_rope * inches_per_foot

    # FA
    answer = total_inches_rope
    return answer