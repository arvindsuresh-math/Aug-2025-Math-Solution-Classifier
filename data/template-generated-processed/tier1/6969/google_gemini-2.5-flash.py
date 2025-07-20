def solve():
    """Index: 6969.
    Returns: the total number of tickets Turner needs.
    """
    # L1
    rollercoaster_rides = 3 # rollercoaster 3 times
    tickets_per_rollercoaster_ride = 4 # 4 tickets to ride the rollercoaster
    tickets_for_rollercoaster = rollercoaster_rides * tickets_per_rollercoaster_ride

    # L2
    catapult_rides = 2 # the Catapult 2 times
    tickets_per_catapult_ride = 4 # 4 tickets to ride the Catapult
    tickets_for_catapult = catapult_rides * tickets_per_catapult_ride

    # L3
    ferris_wheel_rides = 1 # the Ferris wheel once
    tickets_per_ferris_wheel_ride = 1 # 1 ticket to ride the Ferris wheel
    tickets_for_ferris_wheel = ferris_wheel_rides * tickets_per_ferris_wheel_ride

    # L4
    total_tickets = tickets_for_rollercoaster + tickets_for_catapult + tickets_for_ferris_wheel

    # FA
    answer = total_tickets
    return answer