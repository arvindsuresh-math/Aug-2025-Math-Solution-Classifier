def solve():
    """Index: 2930.
    Returns: the total amount the aqua park earns from both groups.
    """
    # L1
    admission_fee = 12 # $12 admission
    tour_fee = 6 # $6 for a tour
    group1_size = 10 # group of 10 people
    group1_per_person = admission_fee + tour_fee

    # L2
    group1_total = group1_per_person * group1_size

    # L3
    group2_size = 5 # group of 5 people
    group2_total = admission_fee * group2_size

    # L4
    total_earnings = group1_total + group2_total

    # FA
    answer = total_earnings
    return answer