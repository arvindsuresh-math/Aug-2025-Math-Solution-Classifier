def solve():
    """Index: 2468.
    Returns: the number of sessions the remaining patients need.
    """
    # L1
    patient_one_sessions = 6 # One of the patients needs 6 sessions
    patient_two_more_than_one = 5 # 5 more than that
    patient_two_sessions = patient_one_sessions + patient_two_more_than_one

    # L2
    first_two_patients_total_sessions = patient_one_sessions + patient_two_sessions

    # L3
    total_sessions_needed = 25 # 25 sessions in total
    remaining_patients_sessions = total_sessions_needed - first_two_patients_total_sessions

    # FA
    answer = remaining_patients_sessions
    return answer