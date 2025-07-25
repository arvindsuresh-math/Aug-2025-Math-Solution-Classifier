def solve():
    """Index: 1978.
    Returns: the total number of miles Alice will have walked by Friday.
    """
    # L1
    miles_to_school = 10 # walks 10 miles through a large grass field to get to school
    miles_home = 12 # walks 12 miles through a forest
    monday_total = miles_to_school + miles_home

    # L2
    num_other_days = 4 # the other 4 days, from Tuesday to Friday
    other_days_total = num_other_days * monday_total

    # L3
    total_miles = monday_total + other_days_total

    # FA
    answer = total_miles
    return answer