def solve():
    """Index: 2930.
    Returns: the total earnings of the aqua park.
    """
    # L1
    admission_charge = 12 # $12 admission
    tour_charge = 6 # $6 for a tour
    cost_per_person_with_tour = admission_charge + tour_charge

    # L2
    group_size_with_tour = 10 # A group of 10 people
    total_cost_group_with_tour = cost_per_person_with_tour * group_size_with_tour

    # L3
    group_size_admission_only = 5 # a group of 5 people
    total_cost_group_admission_only = admission_charge * group_size_admission_only

    # L4
    total_earnings = total_cost_group_with_tour + total_cost_group_admission_only

    # FA
    answer = total_earnings
    return answer