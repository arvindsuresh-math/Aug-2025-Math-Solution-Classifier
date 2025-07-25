def solve():
    """Index: 2831.
    Returns: the number of schools Mandy was accepted to.
    """
    # L1
    total_med_schools = 42 # 42 med schools
    applied_fraction_denominator = 3 # 1/3 of the schools
    schools_applied_to = total_med_schools / applied_fraction_denominator

    # L2
    accepted_divisor = 2 # half of the schools
    schools_accepted_to = schools_applied_to / accepted_divisor

    # FA
    answer = schools_accepted_to
    return answer