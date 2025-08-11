from fractions import Fraction

def solve():
    """Index: 4400.
    Returns: the total time to complete the hike in minutes.
    """
    # L1
    total_trail_length = 5 # The trail is 5 miles long
    uphill_percent_decimal = 0.6 # 60% is uphill
    uphill_miles = total_trail_length * uphill_percent_decimal

    # L2
    uphill_speed = 2 # uphill at 2 MPH
    uphill_hours = uphill_miles / uphill_speed

    # L3
    minutes_per_hour = 60 # WK
    uphill_minutes = uphill_hours * minutes_per_hour

    # L4
    total_percent = 100 # WK
    uphill_percent = 60 # 60% is uphill
    downhill_percent = total_percent - uphill_percent

    # L5
    downhill_percent_decimal = 0.4 # the rest is downhill
    downhill_miles = total_trail_length * downhill_percent_decimal

    # L6
    downhill_speed = 3 # downhill at 3MPH
    downhill_hours = Fraction(downhill_miles, downhill_speed)

    # L7
    downhill_minutes = minutes_per_hour * downhill_hours

    # L8
    total_minutes = uphill_minutes + downhill_minutes

    # FA
    answer = total_minutes
    return answer