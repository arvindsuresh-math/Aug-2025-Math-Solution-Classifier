def solve():
    """Index: 5082.
    Returns: the total money Lauren made.
    """
    # L1
    commercial_rate = 0.50 # $0.50 for every commercial
    commercial_views = 100 # 100 people watched commercials
    commercial_revenue = commercial_rate * commercial_views

    # L2
    subscriber_rate = 1.00 # $1.00 for every person who subscribes
    new_subscribers = 27 # 27 people subscribed
    subscriber_revenue = subscriber_rate * new_subscribers

    # L3
    total_money_made = commercial_revenue + subscriber_revenue

    # FA
    answer = total_money_made
    return answer