def solve():
    """Index: 2745.
    Returns: the number of doughnuts left after the staff meeting.
    """
    # L1
    num_staff = 19 # 19 staff
    doughnuts_per_staff = 2 # each of the 19 staff ate 2 doughnuts
    total_eaten = num_staff * doughnuts_per_staff

    # L2
    total_doughnuts = 50 # 50 doughnuts were served
    doughnuts_left = total_doughnuts - total_eaten

    # FA
    answer = doughnuts_left
    return answer