def solve():
    """Index: 6214.
    Returns: the average speed of the planes.
    """
    # L1
    passengers_plane1 = 50 # The first plane has 50
    speed_reduction_per_passenger = 2 # each passenger makes it go 2 MPH slower
    speed_reduction_plane1 = passengers_plane1 * speed_reduction_per_passenger

    # L2
    empty_plane_speed = 600 # An empty plane can go 600 MPH
    speed_plane1 = empty_plane_speed - speed_reduction_plane1

    # L3
    passengers_plane2 = 60 # the second had 60
    speed_reduction_plane2 = passengers_plane2 * speed_reduction_per_passenger

    # L4
    speed_plane2 = empty_plane_speed - speed_reduction_plane2

    # L5
    passengers_plane3 = 40 # the third has 40
    speed_reduction_plane3 = passengers_plane3 * speed_reduction_per_passenger

    # L6
    speed_plane3 = empty_plane_speed - speed_reduction_plane3

    # L7
    total_speed = speed_plane1 + speed_plane2 + speed_plane3

    # L8
    number_of_planes = 3 # Three planes
    average_speed = total_speed / number_of_planes

    # FA
    answer = average_speed
    return answer