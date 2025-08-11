def solve():
    """Index: 5983.
    Returns: the total number of people at the beach according to the solution's logic.
    """
    # L1
    num_parents = 2 # Molly and her parents
    num_molly = 1 # Molly and her parents
    initial_group = num_parents + num_molly

    # L2
    people_joined = 100 # saw 100 people join them
    after_joining = initial_group + people_joined

    # L3
    people_left = 40 # 40 people left the beach
    final_people = after_joining - people_left

    # FA
    answer = final_people
    return answer