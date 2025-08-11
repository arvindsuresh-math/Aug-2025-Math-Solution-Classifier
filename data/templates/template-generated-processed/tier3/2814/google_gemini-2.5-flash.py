def solve():
    """Index: 2814.
    Returns: the number of minutes Josie spent shopping instead of waiting.
    """
    # L1
    minutes_per_hour = 60 # WK
    trip_duration_hours_and_half = 1.5 # an hour and a half
    total_trip_minutes = trip_duration_hours_and_half * minutes_per_hour

    # L2
    wait_cart = 3 # wait 3 minutes for a cart
    wait_unlock_cabinet = 13 # 13 minutes for an employee to unlock a cabinet
    wait_restock_shelf = 14 # 14 minutes for a stocker to restock a shelf
    wait_checkout_line = 18 # 18 minutes in line to check out
    total_waiting_minutes = wait_cart + wait_unlock_cabinet + wait_restock_shelf + wait_checkout_line

    # L3
    shopping_minutes = total_trip_minutes - total_waiting_minutes

    # FA
    answer = shopping_minutes
    return answer