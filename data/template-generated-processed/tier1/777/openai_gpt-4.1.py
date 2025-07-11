def solve():
    """Index: 777.
    Returns: the total amount of money Mara and Riley spent at the carnival.
    """
    # L1
    bumper_car_ticket = 2 # a ticket for a bumper car cost $2
    mara_bumper_car_rides = 2 # Mara rode the bumper car two times
    mara_bumper_car_total = bumper_car_ticket * mara_bumper_car_rides

    # L2
    space_shuttle_ticket = 4 # a ticket for a space shuttle cost $4
    riley_space_shuttle_rides = 4 # Riley rode the space shuttle four times
    riley_space_shuttle_total = space_shuttle_ticket * riley_space_shuttle_rides

    # L3
    ferris_wheel_ticket = 5 # a ticket for a Ferris wheel cost $5
    ferris_wheel_rides_each = 3 # they both rode the Ferris wheel three times
    ferris_wheel_total_per_person = ferris_wheel_ticket * ferris_wheel_rides_each

    # L4
    num_people = 2 # both Mara and Riley
    ferris_wheel_total = ferris_wheel_total_per_person * num_people

    # L5
    total_spent = mara_bumper_car_total + riley_space_shuttle_total + ferris_wheel_total

    # FA
    answer = total_spent
    return answer