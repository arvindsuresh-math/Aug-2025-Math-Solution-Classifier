def solve():
    """Index: 7028.
    Returns: the number of people who will win a prize.
    """
    # L1
    total_audience = 100 # 100 people
    envelope_percent_decimal = 0.40 # 40% of these people
    people_with_envelope = envelope_percent_decimal * total_audience

    # L2
    win_percent_decimal = 0.20 # 20% of these people
    winners = win_percent_decimal * people_with_envelope

    # FA
    answer = winners
    return answer