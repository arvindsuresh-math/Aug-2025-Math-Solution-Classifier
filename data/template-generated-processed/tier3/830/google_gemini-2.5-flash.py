def solve():
    """Index: 830.
    Returns: the percentage of students present in school.
    """
    # L1
    total_percentage = 100 # WK
    home_learners_percentage = 40 # Forty percent of the students have elected to learn from home
    remaining_percentage = total_percentage - home_learners_percentage

    # L2
    groups_divisor = 2 # divided into two equal groups, only one of which is physically in school
    present_percentage = remaining_percentage / groups_divisor

    # FA
    answer = present_percentage
    return answer