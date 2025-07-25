def solve():
    """Index: 140.
    Returns: the number of kids who got into the movie.
    """
    # L1
    riverside_kids = 120 # 120 kids from Riverside High
    riverside_reject_percent_num = 20 # 20% denied from Riverside High
    percent_factor = 0.01 # WK
    riverside_rejected = riverside_reject_percent_num * percent_factor * riverside_kids

    # L2
    westside_kids = 90 # 90 kids from West Side High
    westside_reject_percent_num = 70 # 70% denied from West Side High
    westside_rejected = westside_reject_percent_num * percent_factor * westside_kids

    # L3
    mountaintop_kids = 50 # 50 kids from Mountaintop High
    mountaintop_reject_divisor = 2 # half the 50 kids from Mountaintop High
    mountaintop_rejected = mountaintop_kids / mountaintop_reject_divisor

    # L4
    total_kids = riverside_kids + westside_kids + mountaintop_kids

    # L5
    kids_got_in = total_kids - riverside_rejected - westside_rejected - mountaintop_rejected

    # FA
    answer = kids_got_in
    return answer