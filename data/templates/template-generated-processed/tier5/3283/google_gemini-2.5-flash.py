def solve():
    """Index: 3283.
    Returns: the size of the master bedroom suite.
    """
    # L1
    total_house_sq_ft = 2300 # house is 2,300 sq ft total
    non_bedroom_sq_ft = 1000 # non-bedroom sections take up 1,000 sq ft
    remaining_sq_ft_for_bedrooms = total_house_sq_ft - non_bedroom_sq_ft

    # L4
    # The problem states "guest bedroom is a quarter of the size of the master bedroom suite",
    # implying the master bedroom is 1x and the guest bedroom is 0.25x.
    guest_bedroom_fraction = 0.25 # a quarter of the size
    master_bedroom_coefficient = 1 # WK
    combined_bedroom_coefficient = master_bedroom_coefficient + guest_bedroom_fraction

    # L6
    master_bedroom_suite_size = remaining_sq_ft_for_bedrooms / combined_bedroom_coefficient

    # FA
    answer = master_bedroom_suite_size
    return answer