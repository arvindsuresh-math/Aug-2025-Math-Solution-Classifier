def solve():
    """Index: 7284.
    Returns: the total miles Talia drives that day.
    """
    # L1
    miles_to_park = 5 # 5 miles from Talia's house
    miles_park_to_store = 3 # 3 miles away from the park
    miles_to_store = miles_to_park + miles_park_to_store

    # L2
    miles_store_to_home = 8 # 8 miles from her home
    total_miles = miles_store_to_home + miles_to_store

    # FA
    answer = total_miles
    return answer