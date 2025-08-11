def solve():
    """Index: 2484.
    Returns: the number of people left relaxing on the beach.
    """
    # L1
    initial_people_row1 = 24 # 24 people
    people_leave_row1 = 3 # 3 people get up to wade in the water
    remaining_row1 = initial_people_row1 - people_leave_row1

    # L2
    initial_people_row2 = 20 # originally held 20 people
    people_leave_row2 = 5 # 5 people from the second row... go to join them
    remaining_row2 = initial_people_row2 - people_leave_row2

    # L3
    initial_people_row3 = 18 # The third row is made up of 18 people
    total_remaining = remaining_row1 + remaining_row2 + initial_people_row3

    # FA
    answer = total_remaining
    return answer