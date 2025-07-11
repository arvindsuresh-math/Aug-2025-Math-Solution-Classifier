def solve():
    """Index: 2050.
    Returns: the total number of days John spent protesting.
    """
    # L1
    first_protest_duration = 4 # attends a protest for 4 days
    longer_percent_decimal = 0.25 # 25% longer
    second_protest_longer_duration = first_protest_duration * longer_percent_decimal

    # L2
    second_protest_total_duration = first_protest_duration + second_protest_longer_duration

    # L3
    total_protest_days = first_protest_duration + second_protest_total_duration

    # FA
    answer = total_protest_days
    return answer