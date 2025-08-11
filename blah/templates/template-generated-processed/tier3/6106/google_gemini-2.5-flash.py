def solve():
    """Index: 6106.
    Returns: the average weight of all men and women.
    """
    # L1
    num_men = 8 # 8 men
    avg_weight_men = 190 # average weight of 190 pounds
    total_weight_men = num_men * avg_weight_men

    # L2
    num_women = 6 # 6 women
    avg_weight_women = 120 # average weight of 120 pounds
    total_weight_women = num_women * avg_weight_women

    # L3
    total_people = 14 # all 14 men and women
    total_combined_weight = total_weight_men + total_weight_women

    # L4
    average_weight = total_combined_weight / total_people

    # FA
    answer = average_weight
    return answer