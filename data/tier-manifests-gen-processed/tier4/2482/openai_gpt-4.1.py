def solve():
    """Index: 2482.
    Returns: the number of minutes it takes Jenna to hem her dress.
    """
    # L1
    hem_length_feet = 3 # The dress's hem is 3 feet long
    inches_per_foot = 12 # WK
    hem_length_inches = hem_length_feet * inches_per_foot

    # L2
    stitch_length_inches = 0.25 # Each stitch Jenna makes is 1/4 inch long
    num_stitches = hem_length_inches / stitch_length_inches

    # L3
    stitches_per_minute = 24 # Jenna makes 24 stitches per minute
    minutes = num_stitches / stitches_per_minute

    # FA
    answer = minutes
    return answer