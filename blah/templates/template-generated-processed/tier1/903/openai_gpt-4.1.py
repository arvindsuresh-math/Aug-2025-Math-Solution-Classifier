def solve():
    """Index: 903.
    Returns: the total amount of money Margaux will collect after 7 days.
    """
    # L1
    friend_per_day = 5 # Her friend pays her $5 per day
    num_days = 7 # after 7 days
    friend_total = friend_per_day * num_days

    # L2
    brother_per_day = 8 # her brother $8 per day
    brother_total = brother_per_day * num_days

    # L3
    cousin_per_day = 4 # her cousin $4 per day
    cousin_total = cousin_per_day * num_days

    # L4
    total_collected = friend_total + brother_total + cousin_total

    # FA
    answer = total_collected
    return answer