def solve():
    """Index: 2482.
    Returns: the number of minutes it takes Jenna to hem her dress.
    """
    # L1
    dress_hem_feet = 3 # The dress's hem is 3 feet long
    inches_per_foot = 12 # WK
    dress_hem_inches = dress_hem_feet * inches_per_foot

    # L2
    stitch_length_inches = 0.25 # Each stitch Jenna makes is 1/4 inch long
    total_stitches = dress_hem_inches / stitch_length_inches

    # L3
    stitches_per_minute = 24 # Jenna makes 24 stitches per minute
    time_minutes = total_stitches / stitches_per_minute

    # FA
    answer = time_minutes
    return answer