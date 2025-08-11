def solve():
    """Index: 5492.
    Returns: the number of cookies John has left.
    """
    # L1
    num_dozen_bought = 2 # 2 dozen cookies
    dozen = 12 # WK
    total_cookies = num_dozen_bought * dozen

    # L2
    cookies_eaten = 3 # He eats 3
    cookies_left = total_cookies - cookies_eaten

    # FA
    answer = cookies_left
    return answer