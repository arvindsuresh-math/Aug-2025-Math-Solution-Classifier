def solve():
    """Index: 128.
    Returns: the number of rooms the principal needs to book.
    """
    # L1
    num_queen_beds_per_room = 2 # two queen size beds
    students_per_queen_bed = 2 # which can fit two students each
    students_per_couch = 1 # a pull-out couch, which can fit one student
    students_per_room = num_queen_beds_per_room * students_per_queen_bed + students_per_couch

    # L2
    total_students = 30 # a class of 30 students
    rooms_needed = total_students / students_per_room

    # FA
    answer = rooms_needed
    return answer