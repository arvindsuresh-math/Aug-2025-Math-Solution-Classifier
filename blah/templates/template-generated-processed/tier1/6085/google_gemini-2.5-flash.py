def solve():
    """Index: 6085.
    Returns: the number of gallons of water still left in the pool at the end of five hours.
    """
    # L1
    rate_first_hour = 8 # 8 gallons of water per hour
    gallons_first_hour = rate_first_hour

    # L2
    rate_second_hour = 10 # 10 gallons of water per hour
    gallons_second_hour = rate_second_hour

    # L3
    gallons_third_hour = rate_second_hour

    # L4
    rate_fourth_hour = 14 # 14 gallons of water per hour
    gallons_fourth_hour = rate_fourth_hour

    # L5
    total_gallons_added_by_fourth_hour = gallons_first_hour + gallons_second_hour + gallons_third_hour + gallons_fourth_hour

    # L6
    gallons_lost_fifth_hour = 8 # loses 8 gallons of water
    gallons_remaining = total_gallons_added_by_fourth_hour - gallons_lost_fifth_hour

    # FA
    answer = gallons_remaining
    return answer