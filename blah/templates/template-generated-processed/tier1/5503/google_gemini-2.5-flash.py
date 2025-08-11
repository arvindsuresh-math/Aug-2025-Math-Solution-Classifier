def solve():
    """Index: 5503.
    Returns: the difference between the number of biscuits and butter cookies baked.
    """
    # L1
    butter_cookies_morning = 20 # twenty butter cookies
    butter_cookies_afternoon = 10 # ten butter cookies
    total_butter_cookies = butter_cookies_morning + butter_cookies_afternoon

    # L2
    biscuits_morning = 40 # forty biscuits
    biscuits_afternoon = 20 # twenty biscuits
    total_biscuits = biscuits_morning + biscuits_afternoon

    # L3
    difference = total_biscuits - total_butter_cookies

    # FA
    answer = difference
    return answer