def solve():
    """Index: 2117.
    Returns: the total combined time for both friends to run 5 miles each.
    """
    # L1
    first_runner_initial_time = 21 # The first one runs it in 21 minutes
    initial_distance = 3 # racing three miles
    first_runner_pace = first_runner_initial_time / initial_distance

    # L2
    second_runner_initial_time = 24 # The second one runs it in 24 minutes
    second_runner_pace = second_runner_initial_time / initial_distance

    # L3
    target_distance = 5 # run 5 miles each
    first_runner_total_time = target_distance * first_runner_pace

    # L4
    second_runner_total_time = target_distance * second_runner_pace

    # L5
    total_combined_time = first_runner_total_time + second_runner_total_time

    # FA
    answer = total_combined_time
    return answer