def solve():
    """Index: 3116.
    Returns: the number of people who landed in Virginia.
    """
    # L1
    initial_passengers = 124 # 124 passengers
    got_off_texas = 58 # 58 passengers got off
    got_on_texas = 24 # 24 got on
    passengers_after_texas = initial_passengers - got_off_texas + got_on_texas

    # L2
    got_off_nc = 47 # 47 people got off
    got_on_nc = 14 # 14 got on
    passengers_after_nc = passengers_after_texas - got_off_nc + got_on_nc

    # L3
    crew_members = 10 # 10 crew members
    total_people_landed = passengers_after_nc + crew_members

    # FA
    answer = total_people_landed
    return answer