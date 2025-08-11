def solve():
    """Index: 2115.
    Returns: the number of cookies each child will eat.
    """
    # L1
    cookies_per_package = 25 # 25 cookies
    num_packages = 3 # 3 packages of cookies
    total_cookies = cookies_per_package * num_packages

    # L2
    friends_invited = 4 # invited 4 friends
    aku_count = 1 # WK
    num_children = friends_invited + aku_count
    cookies_per_child = total_cookies / num_children

    # FA
    answer = cookies_per_child
    return answer