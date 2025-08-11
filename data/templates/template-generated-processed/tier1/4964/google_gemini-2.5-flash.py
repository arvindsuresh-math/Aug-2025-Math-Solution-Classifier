def solve():
    """Index: 4964.
    Returns: the total number of messages the remaining members would send in a week.
    """
    # L1
    initial_members = 150 # number of members in the group was 150 before the admin removed some
    removed_members = 20 # 20 members of a Facebook group were removed
    remaining_members = initial_members - removed_members

    # L2
    messages_per_member_per_day = 50 # each member posted 50 messages per day
    total_messages_per_day = messages_per_member_per_day * remaining_members

    # L3
    days_in_week = 7 # WK
    total_messages_per_week = total_messages_per_day * days_in_week

    # FA
    answer = total_messages_per_week
    return answer