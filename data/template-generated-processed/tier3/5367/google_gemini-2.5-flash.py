def solve():
    """Index: 5367.
    Returns: the total time in minutes to fill all the balloons.
    """
    # L1
    num_balloons = 52 # 52 balloons
    gallons_per_balloon = 5 # Each balloon holds 5 gallons of air
    total_gallons_needed = num_balloons * gallons_per_balloon

    # L2
    first_rate = 8 # rate of 8 gallons of air per minute
    first_time = 10 # first 10 minutes
    gallons_filled_first_period = first_rate * first_time

    # L3
    second_time = 5 # For the next five minutes
    half_rate_divisor = 2 # half that rate
    gallons_filled_second_period = first_rate / half_rate_divisor * second_time

    # L4
    remaining_gallons = total_gallons_needed - gallons_filled_first_period - gallons_filled_second_period

    # L5
    final_rate = 2 # rate of 2 gallons of air per minute
    time_for_rest = remaining_gallons / final_rate

    # L6
    total_time = first_time + second_time + time_for_rest

    # FA
    answer = total_time
    return answer