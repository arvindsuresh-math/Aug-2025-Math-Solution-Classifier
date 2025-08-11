def solve():
    """Index: 6291.
    Returns: the total number of chocolate cookies Andy had to start with.
    """
    # L1
    andy_ate = 3 # He ate 3 of them
    brother_ate = 5 # gave his little brother 5
    cookies_andy_brother_ate = brother_ate + andy_ate

    # L3
    num_players = 8 # basketball team of eight members
    cookies_basketball_team_ate = num_players ** 2

    # L4
    total_initial_cookies = cookies_basketball_team_ate + cookies_andy_brother_ate

    # FA
    answer = total_initial_cookies
    return answer