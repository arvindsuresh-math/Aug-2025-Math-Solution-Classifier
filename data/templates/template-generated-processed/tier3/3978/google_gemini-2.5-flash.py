def solve():
    """Index: 3978.
    Returns: the total hours James spends writing per week.
    """
    # L1
    pages_per_person_per_day = 5 # writes 5 pages a day
    number_of_people = 2 # to 2 different people
    pages_per_day = pages_per_person_per_day * number_of_people

    # L2
    days_per_week = 7 # WK
    pages_per_week = pages_per_day * days_per_week

    # L3
    pages_per_hour = 10 # writes 10 pages an hour
    hours_per_week = pages_per_week / pages_per_hour

    # FA
    answer = hours_per_week
    return answer