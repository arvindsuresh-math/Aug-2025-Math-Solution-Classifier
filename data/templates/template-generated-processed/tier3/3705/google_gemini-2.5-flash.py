def solve():
    """Index: 3705.
    Returns: the average weight of the ten students.
    """
    # L1
    girls_average_weight = 45 # average weight of five girls is 45 kg
    num_girls = 5 # five girls
    sum_girls_weight = girls_average_weight * num_girls

    # L2
    boys_average_weight = 55 # average weight of five boys is 55 kg
    num_boys = 5 # five boys
    sum_boys_weight = boys_average_weight * num_boys

    # L3
    total_sum_weight = sum_girls_weight + sum_boys_weight

    # L4
    total_students = 10 # ten students
    average_total_weight = total_sum_weight / total_students

    # FA
    answer = average_total_weight
    return answer