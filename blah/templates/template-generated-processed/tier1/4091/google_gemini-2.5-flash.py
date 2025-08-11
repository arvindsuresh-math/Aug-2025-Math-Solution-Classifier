def solve():
    """Index: 4091.
    Returns: the total number of people working at Ryan's office.
    """
    # L1
    women_in_meeting = 6 # 6 women
    women_percentage_reduction_value = 20 # 20%
    percentage_decimal = 0.20 # 20%
    multiplier = 1 / percentage_decimal # WK
    total_women = women_in_meeting * multiplier

    # L2
    sexes_count = 2 # an even number of men and women working there; 2 sexes
    total_people = total_women * sexes_count

    # FA
    answer = total_people
    return answer