def solve():
    """Index: 6205.
    Returns: the number of friends Mark has left after removal.
    """
    # L1
    total_fraction_of_friends = 1 # WK
    kept_percentage_decimal = 0.4 # He keeps 40% of his friends list
    contacted_fraction = total_fraction_of_friends - kept_percentage_decimal

    # L2
    initial_friends_count = 100 # If he had 100 friends
    num_contacted_people = initial_friends_count * contacted_fraction

    # L3
    non_respond_divisor = 2 # Of those only 50% respond (meaning 50% did not respond, which is 1/2)
    num_removed_people = num_contacted_people / non_respond_divisor

    # L4
    friends_remaining = initial_friends_count - num_removed_people

    # FA
    answer = friends_remaining
    return answer