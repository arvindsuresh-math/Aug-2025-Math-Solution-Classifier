def solve():
    """Index: 5842.
    Returns: the total money James makes a month.
    """
    # L1
    initial_subscribers = 150 # 150 subscribers
    gifted_subscribers = 50 # gifted 50 subscribers
    total_subscribers = initial_subscribers + gifted_subscribers

    # L2
    money_per_subscriber = 9 # $9 a month per subscriber
    monthly_earnings = total_subscribers * money_per_subscriber

    # FA
    answer = monthly_earnings
    return answer