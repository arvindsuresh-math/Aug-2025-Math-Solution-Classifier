def solve():
    """Index: 7286.
    Returns: the total number of hours they all have left to finish their homework.
    """
    # L1
    jacob_hours = 18 # If Jacob has 18 hours left to finish his homework
    greg_less_than_jacob = 6 # six hours less than Jacob
    greg_hours = jacob_hours - greg_less_than_jacob

    # L2
    jacob_greg_total = greg_hours + jacob_hours

    # L3
    patrick_less_than_twice_greg = 4 # 4 hours less
    multiplier_for_twice = 2 # twice the amount of time
    twice_greg_hours = greg_hours * multiplier_for_twice

    # L4
    patrick_hours = twice_greg_hours - patrick_less_than_twice_greg

    # L5
    total_hours_all_three = jacob_greg_total + patrick_hours

    # FA
    answer = total_hours_all_three
    return answer