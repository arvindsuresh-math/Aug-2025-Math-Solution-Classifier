def solve():
    """Index: 7427.
    Returns: Joey's age when Beth was Joey's age now.
    """
    # L1
    years_in_future = 5 # In 5 years
    joey_age_now = 9 # Joey is 9 now
    beth_age_now = years_in_future + joey_age_now

    # L2
    years_ago_beth_was_joey_age = beth_age_now - joey_age_now

    # L3
    joey_age_then = joey_age_now - years_ago_beth_was_joey_age

    # FA
    answer = joey_age_then
    return answer