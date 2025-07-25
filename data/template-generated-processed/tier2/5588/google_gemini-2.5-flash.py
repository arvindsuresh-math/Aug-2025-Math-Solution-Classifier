def solve():
    """Index: 5588.
    Returns: the number of additional life vests Alice needs.
    """
    # L1
    num_students = 40 # 40 students
    percent_students_bringing_vests = 0.20 # 20% of her students are bringing life vests
    students_bringing_vests = percent_students_bringing_vests * num_students

    # L2
    vests_on_hand = 20 # 20 life vests on hand
    total_vests_after_students_bring_theirs = vests_on_hand + students_bringing_vests

    # L3
    num_instructors = 10 # 10 instructors
    total_class_members = num_students + num_instructors

    # L4
    additional_vests_needed = total_class_members - total_vests_after_students_bring_theirs

    # FA
    answer = additional_vests_needed
    return answer