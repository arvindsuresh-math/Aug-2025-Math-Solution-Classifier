from fractions import Fraction

def solve():
    """Index: 2759.
    Returns: the total number of minutes Ryan spends commuting to work every week.
    """
    # L1
    bus_time_longer_than_bike = 10 # ten minutes longer
    bike_time = 30 # thirty minutes to bike to work
    bus_time = bus_time_longer_than_bike + bike_time

    # L2
    bus_rides_per_week = 3 # takes the bus three times a week
    total_bus_time = bus_time * bus_rides_per_week

    # L3
    friend_time_cut_fraction = Fraction(2, 3) # cuts two-thirds off his biking time
    time_cut_by_friend = friend_time_cut_fraction * bike_time

    # L4
    friend_drive_time = bike_time - time_cut_by_friend

    # L5
    total_commuting_time = total_bus_time + friend_drive_time + bike_time

    # FA
    answer = total_commuting_time
    return answer