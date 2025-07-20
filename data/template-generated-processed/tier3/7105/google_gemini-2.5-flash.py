def solve():
    """Index: 7105.
    Returns: the number of people in Beacon.
    """
    # L1
    richmond_people = 3000 # Richmond has 3000 people
    more_than_victoria = 1000 # 1000 more people than Victoria
    victoria_people = richmond_people - more_than_victoria

    # L2
    times_as_many = 4 # Victoria has 4 times as many people as Beacon
    beacon_people = victoria_people / times_as_many

    # FA
    answer = beacon_people
    return answer