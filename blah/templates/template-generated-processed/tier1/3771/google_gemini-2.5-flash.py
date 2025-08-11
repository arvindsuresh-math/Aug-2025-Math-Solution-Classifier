def solve():
    """Index: 3771.
    Returns: the total number of seats in Section B.
    """
    # L1
    seats_per_subsection_80 = 80 # 80 seats each
    num_subsections_80 = 3 # 3 subsections
    total_seats_80_subsections = seats_per_subsection_80 * num_subsections_80

    # L2
    seats_60_subsection = 60 # 60 seats
    total_seats_section_A = total_seats_80_subsections + seats_60_subsection

    # L3
    triple_multiplier = 3 # 3 times as many seats
    triple_section_A_seats = total_seats_section_A * triple_multiplier

    # L4
    extra_seats_section_B = 20 # 20 more seats
    total_seats_section_B = triple_section_A_seats + extra_seats_section_B

    # FA
    answer = total_seats_section_B
    return answer