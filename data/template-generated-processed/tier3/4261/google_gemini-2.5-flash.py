def solve():
    """Index: 4261.
    Returns: the number of cups each girl brought.
    """
    # L1
    total_students = 30 # 30 students in Ms. Leech's class
    num_boys = 10 # 10 boys in the class
    num_girls = total_students - num_boys

    # L2
    cups_per_boy = 5 # each boy today brought 5 cups
    total_cups_boys = cups_per_boy * num_boys

    # L3
    total_cups_class = 90 # total number of cups brought by the students in the class is 90
    total_cups_girls = total_cups_class - total_cups_boys

    # L4
    cups_per_girl = total_cups_girls / num_girls

    # FA
    answer = cups_per_girl
    return answer