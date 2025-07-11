def solve():
    """Index: 128.
    Returns: the number of hotel rooms the principal needs to book.
    """
    # L1
    beds_per_room = 2 # Each of the hotel's rooms has two queen size beds
    students_per_bed = 2 # which can fit two students each
    pullout_couch_capacity = 1 # a pull-out couch, which can fit one student
    students_per_room = beds_per_room * students_per_bed + pullout_couch_capacity

    # L2
    total_students = 30 # class of 30 students
    rooms_needed = total_students / students_per_room

    # FA
    answer = rooms_needed
    return answer