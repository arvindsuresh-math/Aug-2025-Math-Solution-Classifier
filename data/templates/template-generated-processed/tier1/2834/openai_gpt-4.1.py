def solve():
    """Index: 2834.
    Returns: the total number of math problems Marvin and Arvin have practiced altogether.
    """
    # L1
    marvin_yesterday = 40 # Marvin solved 40 math problems yesterday
    marvin_today_multiplier = 3 # three times as many as the number of problems he solved yesterday
    marvin_today = marvin_yesterday * marvin_today_multiplier

    # L2
    marvin_total = marvin_today + marvin_yesterday

    # L3
    arvin_multiplier = 2 # Arvin has practiced twice as many as Marvin
    arvin_total = marvin_total * arvin_multiplier

    # L4
    total_practiced = arvin_total + marvin_total

    # FA
    answer = total_practiced
    return answer