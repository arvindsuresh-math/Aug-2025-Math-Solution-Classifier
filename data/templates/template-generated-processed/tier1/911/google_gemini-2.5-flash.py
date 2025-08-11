def solve():
    """Index: 911.
    Returns: the combined time all the alligators walked.
    """
    # L1
    paul_initial_journey_hours = 4 # 4 hours to walk from his home at the River Nile to the Nile Delta
    return_journey_extra_hours = 2 # 2 more hours than Paul took to walk to the Nile Delta
    paul_return_journey_hours = paul_initial_journey_hours + return_journey_extra_hours

    # L2
    paul_total_journey_time = paul_return_journey_hours + paul_initial_journey_hours

    # L3
    num_other_alligators = 6 # six other alligators
    other_alligators_total_time = num_other_alligators * paul_return_journey_hours

    # L4
    combined_alligator_time = paul_total_journey_time + other_alligators_total_time

    # FA
    answer = combined_alligator_time
    return answer