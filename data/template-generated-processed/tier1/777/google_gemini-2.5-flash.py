def solve():
    """Index: 777.
    Returns: the total amount of money Mara and Riley spent at the carnival.
    """
    # L1
    cost_bumper_car = 2 # a ticket for a bumper car cost $2
    mara_rides_bumper_car = 2 # Mara rode the bumper car two times
    mara_bumper_car_cost = cost_bumper_car * mara_rides_bumper_car

    # L2
    cost_space_shuttle = 4 # a ticket for a space shuttle cost $4
    riley_rides_space_shuttle = 4 # Riley rode the space shuttle four times
    riley_space_shuttle_cost = cost_space_shuttle * riley_rides_space_shuttle

    # L3
    cost_ferris_wheel = 5 # a ticket for a Ferris wheel cost $5
    rides_ferris_wheel_each = 3 # they both rode the Ferris wheel three times
    cost_ferris_wheel_per_person = cost_ferris_wheel * rides_ferris_wheel_each

    # L4
    num_people = 2 # Mara and Riley
    total_ferris_wheel_cost = cost_ferris_wheel_per_person * num_people

    # L5
    total_spent = mara_bumper_car_cost + riley_space_shuttle_cost + total_ferris_wheel_cost

    # FA
    answer = total_spent
    return answer