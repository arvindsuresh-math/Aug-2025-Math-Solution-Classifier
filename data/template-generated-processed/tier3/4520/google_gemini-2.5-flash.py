def solve():
    """Index: 4520.
    Returns: the total number of colored pencils the three of them have.
    """
    # L1
    madeline_pencils = 63 # Madeline has 63 colored pencils
    cheryl_madeline_multiplier = 2 # only half of what Cheryl has
    cheryl_pencils = madeline_pencils * cheryl_madeline_multiplier

    # L2
    cyrus_cheryl_divisor = 3 # thrice as many colored pencils as Cyrus
    cyrus_pencils = cheryl_pencils / cyrus_cheryl_divisor

    # L3
    total_pencils = cheryl_pencils + cyrus_pencils + madeline_pencils

    # FA
    answer = total_pencils
    return answer