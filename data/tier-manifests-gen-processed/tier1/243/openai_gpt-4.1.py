def solve():
    """Index: 243.
    Returns: the total number of hours Mckenna stays at work.
    """
    # L1
    start_time = 8 # starts her day at 8:00 a.m.
    office_end_time = 11 # works in her office up to 11:00 a.m.
    office_hours = office_end_time - start_time

    # L2
    meeting_end_time = 13 # joins her team up to 13:00
    meeting_start_time = office_end_time # meeting starts at 11:00
    meeting_hours = meeting_end_time - meeting_start_time

    # L3
    hours_so_far = office_hours + meeting_hours

    # L4
    additional_hours = 2 # works for another two hours
    total_hours = hours_so_far + additional_hours

    # FA
    answer = total_hours
    return answer