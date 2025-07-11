def solve():
    """Index: 2079.
    Returns: the total number of cookies Kristy baked.
    """
    # L1
    cookies_left_at_end = 6 # If there are 6 cookies left
    third_friend_took = 5 # The second and third friends to arrive took 5 cookies each
    cookies_before_third_friend = cookies_left_at_end + third_friend_took

    # L2
    second_friend_took = 5 # The second and third friends to arrive took 5 cookies each
    cookies_before_second_friend = cookies_before_third_friend + second_friend_took

    # L3
    first_friend_took = 3 # Her first friend arrived and took 3 cookies
    cookies_before_first_friend = cookies_before_second_friend + first_friend_took

    # L4
    brother_took = 1 # gave her brother 1 cookie
    cookies_before_brother = cookies_before_first_friend + brother_took

    # L5
    kristy_ate = 2 # She ate 2 of them
    total_baked_cookies = cookies_before_brother + kristy_ate

    # FA
    answer = total_baked_cookies
    return answer