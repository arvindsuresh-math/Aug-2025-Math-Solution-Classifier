def solve():
    """Index: 5265.
    Returns: the total number of individual chocolates Wendy can package in 4 hours.
    """
    # L1
    minutes_per_hour = 60 # WK
    packing_increment_minutes = 5 # 5 minutes
    increments_per_hour = minutes_per_hour / packing_increment_minutes

    # L2
    chocolates_per_dozen = 12 # WK
    dozens_packaged_in_5_minutes = 2 # 2 dozen chocolates in 5 minutes
    chocolates_per_5_minutes = chocolates_per_dozen * dozens_packaged_in_5_minutes

    # L3
    chocolates_per_hour = increments_per_hour * chocolates_per_5_minutes

    # L4
    total_hours = 4 # in 4 hours
    total_chocolates_packaged = chocolates_per_hour * total_hours

    # FA
    answer = total_chocolates_packaged
    return answer