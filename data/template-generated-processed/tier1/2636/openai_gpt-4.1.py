def solve():
    """Index: 2636.
    Returns: the total time for which the five students were late.
    """
    # L1
    charlize_late = 20 # Charlize was 20 minutes late
    friend_more_late = 10 # each ten minutes late than she was
    friend_late = charlize_late + friend_more_late

    # L2
    num_friends = 4 # Four of her classmates
    friends_total_late = num_friends * friend_late

    # L3
    total_late = friends_total_late + charlize_late

    # FA
    answer = total_late
    return answer