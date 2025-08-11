def solve():
    """Index: 6239.
    Returns: the difference in height in inches between Vlad and his sister.
    """
    # L1
    vlad_feet = 6 # Vlad is 6 feet
    vlad_inches_extra = 3 # 3 inches tall
    inches_per_foot = 12 # WK
    vlad_total_inches = vlad_feet * inches_per_foot + vlad_inches_extra

    # L2
    sister_feet = 2 # sister is 2 feet
    sister_inches_extra = 10 # 10 inches tall
    sister_total_inches = sister_feet * inches_per_foot + sister_inches_extra

    # L3
    difference_in_inches = vlad_total_inches - sister_total_inches

    # FA
    answer = difference_in_inches
    return answer