def solve():
    """Index: 2937.
    Returns: the total number of cartons of milk consumed by the students in the lunchroom.
    """
    # L1
    monitors_per_group = 2 # 2 monitors for every 15 students
    students_per_group = 15 # 2 monitors for every 15 students
    # (L1 is not needed for the answer, as the ratio is already given in the question)

    # L2
    num_monitors = 8 # 8 monitors
    students_per_monitor_group = students_per_group # 15 students per 2 monitors
    num_students = num_monitors * (students_per_monitor_group / monitors_per_group)

    # L3
    percent_total = 100 # WK
    percent_girls = 40 # 40% are girls
    percent_boys = percent_total - percent_girls

    # L4
    boys_fraction = percent_boys / percent_total
    num_boys = num_students * boys_fraction

    # L5
    girls_fraction = percent_girls / percent_total
    num_girls = num_students * girls_fraction

    # L6
    milk_per_boy = 1 # every boy drinks, on average, 1 carton of milk
    boys_milk = num_boys * milk_per_boy

    # L7
    milk_per_girl = 2 # every girl drinks, on average, 2 cartons of milk
    girls_milk = num_girls * milk_per_girl

    # L8
    total_milk = boys_milk + girls_milk

    # FA
    answer = total_milk
    return answer