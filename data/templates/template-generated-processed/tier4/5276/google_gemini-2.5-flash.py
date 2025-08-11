def solve():
    """Index: 5276.
    Returns: the new percentage of girls in the class.
    """
    # L1
    total_students = 20 # A 20 person classroom
    girls_percent_num = 40 # 40% girls
    percent_factor = 0.01 # WK
    num_girls = total_students * girls_percent_num * percent_factor

    # L2
    initial_num_boys = total_students - num_girls

    # L3
    new_boys = 5 # 5 new boys
    new_num_boys = initial_num_boys + new_boys
    new_total_students = total_students + new_boys

    # L4
    new_girls_percentage = (num_girls / new_total_students) * 100

    # FA
    answer = new_girls_percentage
    return answer