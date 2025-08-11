def solve():
    """Index: 2195.
    Returns: the total distance Shane drives in an 80 day semester.
    """
    # L1
    trips_per_day = 2 # to school and back
    miles_one_way = 10 # drives a total of 10 miles (one way)
    miles_per_day = trips_per_day * miles_one_way

    # L2
    semester_days = 80 # 80 day semester
    total_miles = semester_days * miles_per_day

    # FA
    answer = total_miles
    return answer