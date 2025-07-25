def solve():
    """Index: 6753.
    Returns: the number of tickets Amanda needs to sell on the third day to meet her goal.
    """
    # L1
    tickets_per_friend = 4 # sells 5 of her friends 4 tickets each
    num_friends = 5 # sells 5 of her friends
    tickets_day1 = tickets_per_friend * num_friends

    # L2
    tickets_day2 = 32 # On the second day she sells 32 tickets
    total_tickets_day2 = tickets_day1 + tickets_day2

    # L3
    goal_tickets = 80 # sell 80 tickets
    tickets_day3_needed = goal_tickets - total_tickets_day2

    # FA
    answer = tickets_day3_needed
    return answer