def solve():
    """Index: 2468.
    Returns: the number of sessions the remaining patients need.
    """
    # L1
    first_patient_sessions = 6 # One of the patients needs 6 sessions
    second_patient_more = 5 # Another patient needs 5 more than that
    second_patient_sessions = first_patient_sessions + second_patient_more

    # L2
    first_two_total = first_patient_sessions + second_patient_sessions

    # L3
    total_sessions = 25 # 25 sessions in total
    remaining_sessions = total_sessions - first_two_total

    # FA
    answer = remaining_sessions
    return answer