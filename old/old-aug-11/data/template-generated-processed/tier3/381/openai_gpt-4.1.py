def solve():
    """Index: 381.
    Returns: the number of minutes Matt worked more on Wednesday than on Tuesday.
    """
    # L1
    monday_minutes = 450 # Matt worked for 450 minutes in his office
    tuesday_divisor = 2 # half the number of minutes he worked on Monday
    tuesday_minutes = monday_minutes / tuesday_divisor

    # L2
    wednesday_minutes = 300 # he worked for 300 minutes
    minutes_more = wednesday_minutes - tuesday_minutes

    # FA
    answer = minutes_more
    return answer