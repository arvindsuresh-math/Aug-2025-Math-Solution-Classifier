def solve():
    """Index: 3887.
    Returns: the average miles per day the second dog walks.
    """
    # L1
    days_per_week = 7 # WK
    first_dog_miles_per_day = 2 # The first dog walks an average of 2 miles a day
    miles_first_dog_per_week = days_per_week * first_dog_miles_per_day

    # L2
    total_miles_per_week = 70 # they walk a total of 70 miles a week
    miles_second_dog_per_week = total_miles_per_week - miles_first_dog_per_week

    # L3
    second_dog_miles_per_day = miles_second_dog_per_week / days_per_week

    # FA
    answer = second_dog_miles_per_day
    return answer