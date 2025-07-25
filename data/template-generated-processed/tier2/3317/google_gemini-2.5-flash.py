def solve():
    """Index: 3317.
    Returns: the number of additional days Hazel can miss without taking exams.
    """
    # L1
    school_year_days = 180 # 180 days in a school year
    max_miss_percent_num = 5 # miss 5%
    max_miss_percent_decimal = 0.05 # from solution text: .05
    total_missable_days = school_year_days * max_miss_percent_decimal

    # L2
    days_missed_already = 6 # missed 6 days of school
    remaining_missable_days = total_missable_days - days_missed_already

    # FA
    answer = remaining_missable_days
    return answer