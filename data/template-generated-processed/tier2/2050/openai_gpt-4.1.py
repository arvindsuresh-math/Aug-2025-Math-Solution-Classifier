def solve():
    """Index: 2050.
    Returns: the total number of days John spent protesting.
    """
    # L1
    first_protest_days = 4 # attends a protest for 4 days
    percent_longer = 0.25 # attends a second protest for 25% longer
    extra_days = first_protest_days * percent_longer

    # L2
    second_protest_days = first_protest_days + extra_days

    # L3
    total_days = first_protest_days + second_protest_days

    # FA
    answer = total_days
    return answer