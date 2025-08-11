def solve():
    """Index: 2201.
    Returns: the total number of roses Uncle Welly planted in his vacant lot.
    """
    # L1
    roses_two_days_ago = 50 # Uncle Welly planted 50 roses on his vacant lot
    more_roses_yesterday = 20 # planted 20 more roses than the previous day
    roses_yesterday = roses_two_days_ago + more_roses_yesterday

    # L2
    multiplier_today = 2 # planted twice the number of roses than two days ago
    roses_today = multiplier_today * roses_two_days_ago

    # L3
    total_roses = roses_two_days_ago + roses_yesterday + roses_today

    # FA
    answer = total_roses
    return answer