def solve():
    """Index: 1263.
    Returns: the number of coins Phil had left after losing some.
    """
    # L1
    initial_coins = 50 # started with 50 state quarters
    doubling_factor = 2 # doubled this
    coins_after_doubling = initial_coins * doubling_factor

    # L2
    coins_per_month_year2 = 3 # collected 3 each month
    months_per_year = 12 # 12 months in a year
    coins_added_year2 = coins_per_month_year2 * months_per_year

    # L3
    coins_per_collection_event_year3 = 1 # collected 1 every third month
    collection_frequency_months_year3 = 3 # every third month
    collection_events_per_year_year3 = months_per_year / collection_frequency_months_year3
    coins_added_year3 = collection_events_per_year_year3 * coins_per_collection_event_year3

    # L4
    total_coins_before_loss = coins_after_doubling + coins_added_year2 + coins_added_year3

    # L5
    loss_denominator = 4 # lost a quarter of them
    coins_lost = total_coins_before_loss / loss_denominator

    # L6
    remaining_coins = total_coins_before_loss - coins_lost

    # FA
    answer = remaining_coins
    return answer