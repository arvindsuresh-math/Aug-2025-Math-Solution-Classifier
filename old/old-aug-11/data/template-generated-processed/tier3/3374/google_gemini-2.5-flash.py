def solve():
    """Index: 3374.
    Returns: the number of insects given to each group.
    """
    # L1
    boys_collected_insects = 200 # The Boys collected 200 insects
    girls_collected_insects = 300 # the girls collected 300 insects
    total_insects_collected = boys_collected_insects + girls_collected_insects

    # L2
    number_of_groups = 4 # divide the class equally into four groups
    insects_per_group = total_insects_collected / number_of_groups

    # FA
    answer = insects_per_group
    return answer