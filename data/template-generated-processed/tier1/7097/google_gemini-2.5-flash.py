def solve():
    """Index: 7097.
    Returns: the total number of cookies Paul and Paula have.
    """
    # L1
    paul_cookies = 45 # bought 45 cookies
    paula_fewer = 3 # bought 3 fewer cookies than Paul
    paula_cookies = paul_cookies - paula_fewer

    # L2
    total_cookies = paula_cookies + paul_cookies

    # FA
    answer = total_cookies
    return answer