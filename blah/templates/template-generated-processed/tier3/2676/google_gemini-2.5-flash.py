def solve():
    """Index: 2676.
    Returns: the number of sweets Jennifer and her friends get each.
    """
    # L1
    green_sweets = 212 # 212 green sweets
    blue_sweets = 310 # 310 blue sweets
    yellow_sweets = 502 # 502 yellow sweets
    total_sweets = green_sweets + blue_sweets + yellow_sweets

    # L2
    num_friends = 3 # 3 friends
    jennifer = 1 # herself
    num_people = jennifer + num_friends
    sweets_per_person = total_sweets / num_people

    # FA
    answer = sweets_per_person
    return answer