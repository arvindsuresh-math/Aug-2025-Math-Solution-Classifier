def solve():
    """Index: 18.
    Returns: the total number of hours Roque takes to get to and from work in a week with walking and biking.
    """
    # L1
    walk_to_work_time = 2 # takes Roque two hours to walk to work
    walk_days = 3 # walks to and from work three times a week
    walk_to_total = walk_to_work_time * walk_days

    # L2
    walk_to_from_total = walk_to_total * 2

    # L3
    bike_to_work_time = 1 # one hour to ride his bike to work
    bike_days = 2 # rides his bike to and from work twice a week
    bike_to_total = bike_to_work_time * bike_days

    # L4
    bike_to_from_total = bike_to_total * 2

    # L5
    total_hours = walk_to_from_total + bike_to_from_total

    # FA
    answer = total_hours
    return answer