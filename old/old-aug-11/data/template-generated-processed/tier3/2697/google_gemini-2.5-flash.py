def solve():
    """Index: 2697.
    Returns: the total inches of thread Shelly needs.
    """
    # L1
    friends_in_classes = 6 # six friends in classes
    half_divisor = 2 # half that number
    friends_from_clubs = friends_in_classes / half_divisor

    # L2
    total_friends = friends_in_classes + friends_from_clubs

    # L3
    thread_per_keychain = 12 # Each keychain takes 12 inches of thread
    total_thread_needed = total_friends * thread_per_keychain

    # FA
    answer = total_thread_needed
    return answer