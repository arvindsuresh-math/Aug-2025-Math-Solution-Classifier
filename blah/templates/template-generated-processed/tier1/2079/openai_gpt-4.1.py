def solve():
    """Index: 2079.
    Returns: the number of cookies Kristy baked.
    """
    # L1
    cookies_left = 6 # there are 6 cookies left
    third_friend_took = 5 # third friends to arrive took 5 cookies
    before_third_friend = cookies_left + third_friend_took

    # L2
    second_friend_took = 5 # second friends to arrive took 5 cookies
    before_second_friend = before_third_friend + second_friend_took

    # L3
    first_friend_took = 3 # first friend arrived and took 3 cookies
    before_first_friend = before_second_friend + first_friend_took

    # L4
    brother_took = 1 # gave her brother 1 cookie
    before_brother = before_first_friend + brother_took

    # L5
    kristy_ate = 2 # She ate 2 of them
    total_baked = before_brother + kristy_ate

    # FA
    answer = total_baked
    return answer