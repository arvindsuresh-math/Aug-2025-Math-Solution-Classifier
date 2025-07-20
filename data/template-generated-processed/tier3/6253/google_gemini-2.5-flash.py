def solve():
    """Index: 6253.
    Returns: the average amount of licks to get to the center of a lollipop.
    """
    # L1
    dan_licks = 58 # Dan can get to the center of a lollipop in 58 licks
    michael_licks = 63 # Micheal does it in 63 licks
    sam_licks = 70 # Sam & David each take 70 licks
    david_licks = 70 # Sam & David each take 70 licks
    lance_licks = 39 # Lance only needs 39 licks
    total_licks = dan_licks + michael_licks + sam_licks + david_licks + lance_licks

    # L2
    number_of_people = 5 # 5 people
    average_licks = total_licks / number_of_people

    # FA
    answer = average_licks
    return answer