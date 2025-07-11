def solve():
    """Index: 1904.
    Returns: the number of items Carla needs to collect each day.
    """
    # L1
    leaves_needed = 30 # collect 30 leaves
    bugs_needed = 20 # and 20 bugs
    total_items = leaves_needed + bugs_needed

    # L2
    days_due = 10 # due in 10 days
    daily_collection_amount = total_items / days_due

    # FA
    answer = daily_collection_amount
    return answer