def solve():
    """Index: 4332.
    Returns: the number of trips Jean makes.
    """
    # L4
    total_trips = 40 # 40 trips total
    jean_extra_trips = 6 # plus 6
    multiplier_for_bill = 2 # WK (from '2b' in the equation 2b + 6 = 40)
    two_times_bill_trips = total_trips - jean_extra_trips

    # L5
    bill_trips = two_times_bill_trips / multiplier_for_bill

    # L6
    jean_trips = bill_trips + jean_extra_trips

    # FA
    answer = jean_trips
    return answer