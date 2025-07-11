def solve():
    """Index: 827.
    Returns: the number of people needed to fill all the chairs in the church.
    """
    # L1
    chairs_per_row = 6 # six chairs in each row
    num_rows = 20 # 20 rows of chairs
    total_chairs = chairs_per_row * num_rows

    # L2
    people_per_chair = 5 # each chair holds five people
    total_people = people_per_chair * total_chairs

    # FA
    answer = total_people
    return answer