def solve():
    """Index: 243.
    Returns: the total number of hours Mckenna stays at work.
    """
    # L1
    end_time_office = 11 # up to 11:00 a.m.
    start_time_office = 8 # 8:00 a.m.
    office_hours = end_time_office - start_time_office

    # L2
    meeting_end_time = 13 # up to 13:00
    meeting_start_time = 11 # up to 11:00 (implicitly, as she joins after office work)
    meeting_hours = meeting_end_time - meeting_start_time

    # L3
    total_hours_so_far = office_hours + meeting_hours

    # L4
    additional_work_hours = 2 # works for another two hours
    total_work_hours = total_hours_so_far + additional_work_hours

    # FA
    answer = total_work_hours
    return answer