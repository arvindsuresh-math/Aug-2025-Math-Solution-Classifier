def solve():
    """Index: 6934.
    Returns: the total number of students Mrs. McGillicuddy had over the two kindergarten sessions.
    """
    # L1
    registered_morning = 25 # 25 students registered for the morning session
    absent_morning = 3 # 3 students were absent
    present_morning = registered_morning - absent_morning

    # L2
    registered_afternoon = 24 # 24 students registered for the afternoon session
    absent_afternoon = 4 # 4 students were absent
    present_afternoon = registered_afternoon - absent_afternoon

    # L3
    total_students = present_morning + present_afternoon

    # FA
    answer = total_students
    return answer