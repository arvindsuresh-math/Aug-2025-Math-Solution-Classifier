def solve():
    """Index: 4167.
    Returns: the total number of donuts Andrew's mother needs to buy.
    """
    # L1
    initial_friends_count = 4 # Andrew is having two of his friends over... Andrew ends up inviting two more friends (2+2=4 friends)
    donuts_per_friend_initial = 3 # buy 3 donuts
    donuts_for_friends_initial = initial_friends_count * donuts_per_friend_initial

    # L2
    extra_donut_per_friend_amount = 1 # buy one more donut for each of Andrew's friends
    donuts_per_friend_with_extra = donuts_per_friend_initial + extra_donut_per_friend_amount

    # L3
    extra_donuts_for_all_friends = initial_friends_count * extra_donut_per_friend_amount
    total_donuts_for_friends = donuts_for_friends_initial + extra_donuts_for_all_friends

    # L4
    donuts_for_andrew = donuts_per_friend_initial + extra_donut_per_friend_amount

    # L5
    total_donuts_needed = total_donuts_for_friends + donuts_for_andrew

    # FA
    answer = total_donuts_needed
    return answer