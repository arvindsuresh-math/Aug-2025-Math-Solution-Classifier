def solve():
    """Index: 7372.
    Returns: the total distance between city A and city D.
    """
    # L1
    dist_AB = 100 # The distance between city A and city B is 100 miles
    dist_BC_more_than_AB = 50 # city B and C are 50 more miles apart than city A and B
    dist_BC = dist_AB + dist_BC_more_than_AB

    # L2
    dist_AC = dist_AB + dist_BC

    # L3
    multiplier_CD_BC = 2 # twice the distance between city B and city C
    dist_CD = multiplier_CD_BC * dist_BC

    # L4
    total_distance_AD = dist_AC + dist_CD

    # FA
    answer = total_distance_AD
    return answer