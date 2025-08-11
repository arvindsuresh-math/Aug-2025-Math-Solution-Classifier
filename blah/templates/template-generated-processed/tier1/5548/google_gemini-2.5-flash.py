def solve():
    """Index: 5548.
    Returns: the number of hours Kira was away from home.
    """
    # L1
    initial_kibble = 3 # fills her cat's bowl with 3 pounds of kibble
    remaining_kibble = 1 # there is still 1 pound left
    eaten_kibble = initial_kibble - remaining_kibble

    # L2
    hours_per_pound = 4 # eats a pound of kibble every 4 hours
    total_hours_away = hours_per_pound * eaten_kibble

    # FA
    answer = total_hours_away
    return answer