def solve():
    """Index: 2745.
    Returns: the number of doughnuts left.
    """
    # L1
    num_staff = 19 # 19 staff
    doughnuts_per_staff = 2 # ate 2 doughnuts
    doughnuts_eaten = num_staff * doughnuts_per_staff

    # L2
    total_doughnuts_served = 50 # 50 doughnuts were served
    doughnuts_left = total_doughnuts_served - doughnuts_eaten

    # FA
    answer = doughnuts_left
    return answer