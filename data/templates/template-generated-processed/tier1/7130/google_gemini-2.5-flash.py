def solve():
    """Index: 7130.
    Returns: the number of people lifting weights at the start of Bethany's shift.
    """
    # L1
    people_came_in = 5 # 5 more people came in
    people_left = 2 # 2 people left
    net_change = people_came_in - people_left

    # L2
    people_now = 19 # 19 people in the gym
    initial_people = people_now - net_change

    # FA
    answer = initial_people
    return answer