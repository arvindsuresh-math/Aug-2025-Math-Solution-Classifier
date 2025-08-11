def solve():
    """Index: 3601.
    Returns: the total gallons of water Nicole will need in four weeks.
    """
    # L1
    first_two_tanks_gallons_each = 8 # The first two tanks need 8 gallons of water each
    num_first_tanks = 2 # The first two tanks
    gallons_first_two_tanks = first_two_tanks_gallons_each * num_first_tanks

    # L2
    fewer_gallons = 2 # 2 fewer gallons of water each than the first two tanks
    gallons_other_tanks_each = first_two_tanks_gallons_each - fewer_gallons

    # L3
    num_other_tanks = 2 # the other two need
    gallons_other_two_tanks = gallons_other_tanks_each * num_other_tanks

    # L4
    gallons_per_week = gallons_first_two_tanks + gallons_other_two_tanks

    # L5
    num_weeks = 4 # in four weeks
    total_gallons_four_weeks = gallons_per_week * num_weeks

    # FA
    answer = total_gallons_four_weeks
    return answer