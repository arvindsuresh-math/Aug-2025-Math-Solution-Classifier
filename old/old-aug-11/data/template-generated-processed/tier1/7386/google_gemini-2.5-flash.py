def solve():
    """Index: 7386.
    Returns: the number of children on the airplane.
    """
    # L1
    num_men = 30 # 30 men
    num_women = 30 # number of men and women is equal
    total_men_women = num_men + num_women

    # L2
    total_passengers = 80 # 80 passengers
    num_children = total_passengers - total_men_women

    # FA
    answer = num_children
    return answer