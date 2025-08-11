def solve():
    """Index: 3938.
    Returns: the number of brownies each person can eat.
    """
    # L1
    columns = 6 # 6 even columns
    rows = 3 # 3 even rows
    total_brownies = columns * rows

    # L2
    num_people = 6 # 6 people, including Frank, in total
    brownies_per_person = total_brownies / num_people

    # FA
    answer = brownies_per_person
    return answer