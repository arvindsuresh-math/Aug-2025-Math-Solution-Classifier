def solve():
    """Index: 4388.
    Returns: the average page count per essay.
    """
    # L1
    first_group_pages = 2 # 2 pages
    first_group_students = 5 # first 5 students
    total_pages_first_group = first_group_pages * first_group_students

    # L2
    second_group_pages = 3 # 3 pages
    second_group_students = 5 # next 5 students
    total_pages_second_group = second_group_pages * second_group_students

    # L3
    third_group_pages = 1 # 1 page
    third_group_students = 5 # last 5 students
    total_pages_third_group = third_group_pages * third_group_students

    # L4
    total_pages_all_students = total_pages_first_group + total_pages_second_group + total_pages_third_group

    # L5
    total_students = 15 # 15 students
    average_page_count = total_pages_all_students / total_students

    # FA
    answer = average_page_count
    return answer