def solve():
    """Index: 5419.
    Returns: the number of kids who came to the cookout in 2004.
    """
    # L1
    kids_2006 = 20 # If there were 20 kids at the cookout in 2006
    numerator_2006_to_2005 = 2 # 2/3 as many kids came to the cookout as in 2005
    denominator_2006_to_2005 = 3 # 2/3 as many kids came to the cookout as in 2005
    kids_2005 = kids_2006 / numerator_2006_to_2005 * denominator_2006_to_2005

    # L2
    half_factor = 2 # half the number of kids came to the cookout as compared to 2004
    kids_2004 = kids_2005 * half_factor

    # FA
    answer = kids_2004
    return answer