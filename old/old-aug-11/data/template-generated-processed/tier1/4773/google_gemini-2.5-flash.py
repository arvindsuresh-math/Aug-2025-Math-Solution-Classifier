def solve():
    """Index: 4773.
    Returns: the total number of doctors and nurses left.
    """
    # L1
    initial_doctors = 11 # 11 doctors
    doctors_quit = 5 # 5 doctors ... quit
    doctors_left = initial_doctors - doctors_quit

    # L2
    initial_nurses = 18 # 18 nurses
    nurses_quit = 2 # 2 nurses quit
    nurses_left = initial_nurses - nurses_quit

    # L3
    total_left = doctors_left + nurses_left

    # FA
    answer = total_left
    return answer