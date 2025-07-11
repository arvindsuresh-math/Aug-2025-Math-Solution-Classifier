def solve():
    """Index: 140.
    Returns: the number of kids who got into the movie.
    """
    # L1
    riverside_percent_num = 20 # 20% of the 120 kids from Riverside High
    riverside_total_kids = 120 # 120 kids from Riverside High
    percent_factor = 0.01 # WK
    riverside_rejected_kids = riverside_percent_num * percent_factor * riverside_total_kids

    # L2
    westside_percent_num = 70 # 70% of the 90 kids from West Side High
    westside_total_kids = 90 # 90 kids from West Side High
    westside_rejected_kids = westside_percent_num * percent_factor * westside_total_kids

    # L3
    mountaintop_total_kids = 50 # 50 kids from Mountaintop High
    mountaintop_divisor = 2 # half the 50 kids from Mountaintop High
    mountaintop_rejected_kids = mountaintop_total_kids / mountaintop_divisor

    # L4
    total_initial_kids = riverside_total_kids + westside_total_kids + mountaintop_total_kids

    # L5
    kids_who_got_in = total_initial_kids - riverside_rejected_kids - westside_rejected_kids - mountaintop_rejected_kids

    # FA
    answer = kids_who_got_in
    return answer