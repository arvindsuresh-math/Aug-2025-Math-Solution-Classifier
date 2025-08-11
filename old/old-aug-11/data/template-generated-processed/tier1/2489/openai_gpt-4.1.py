def solve():
    """Index: 2489.
    Returns: the total number of alligators Samara and her friends saw.
    """
    # L1
    num_friends = 3 # three of her friends
    avg_alligators_per_friend = 10 # average of 10 alligators each
    total_friends_alligators = num_friends * avg_alligators_per_friend

    # L2
    samara_alligators = 20 # Samara had seen 20 alligators
    total_alligators = total_friends_alligators + samara_alligators

    # FA
    answer = total_alligators
    return answer