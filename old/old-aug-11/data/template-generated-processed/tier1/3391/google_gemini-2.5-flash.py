def solve():
    """Index: 3391.
    Returns: the number of days Kelly spent at her sister's house.
    """
    # L1
    num_weeks = 3 # three week vacation
    days_per_week = 7 # WK
    total_vacation_days = days_per_week * num_weeks

    # L2
    travel_to_grandparents = 1 # The first day, she spent traveling
    travel_to_brother = 1 # The next day, she spent traveling
    travel_to_sister = 2 # two days traveling to her sister's house
    travel_home = 2 # two more days traveling home
    total_travel_days = travel_to_grandparents + travel_to_brother + travel_to_sister + travel_home

    # L3
    days_at_grandparents = 5 # next 5 days she spent at her Grandparents' house
    days_at_brother = 5 # next 5 days at her brother's house
    total_relative_days_excluding_sister = days_at_grandparents + days_at_brother

    # L4
    days_at_sister_house = total_vacation_days - total_travel_days - total_relative_days_excluding_sister

    # FA
    answer = days_at_sister_house
    return answer