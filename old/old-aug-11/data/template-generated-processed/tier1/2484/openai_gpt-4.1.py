def solve():
    """Index: 2484.
    Returns: the number of people left relaxing on the beach.
    """
    # L1
    first_row_initial = 24 # first row is made up of 24 people
    first_row_left = 3 # 3 people get up to wade in the water
    first_row_now = first_row_initial - first_row_left

    # L2
    second_row_initial = 20 # second row, which originally held 20 people
    second_row_left = 5 # 5 people from the second row ... go to join them
    second_row_now = second_row_initial - second_row_left

    # L3
    third_row = 18 # third row is made up of 18 people
    total_people = first_row_now + second_row_now + third_row

    # FA
    answer = total_people
    return answer