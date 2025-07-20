def solve():
    """Index: 6289.
    Returns: the total number of job applications sent.
    """
    # L1
    applications_in_state = 200 # 200 job applications to companies in her state
    multiplier_other_states = 2 # twice that number
    applications_other_states = applications_in_state * multiplier_other_states

    # L2
    total_applications = applications_other_states + applications_in_state

    # FA
    answer = total_applications
    return answer