def solve():
    """Index: 6746.
    Returns: the number of additional members the club needs.
    """
    # L1
    current_members = 10 # club has 10 members now
    multiplier_for_twice = 2 # twice their current number
    twice_current_members = current_members * multiplier_for_twice

    # L2
    additional_five = 5 # 5 more than twice their current number
    desired_total_members = twice_current_members + additional_five

    # L3
    additional_members_needed = desired_total_members - current_members

    # FA
    answer = additional_members_needed
    return answer