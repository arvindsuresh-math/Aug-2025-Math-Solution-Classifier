def solve():
    """Index: 6610.
    Returns: the number of eggs Mortdecai donates to the charity.
    """
    # L1
    collects_per_day = 8 # collects 8 dozen eggs every Tuesday and Thursday
    num_collection_days = 2 # every Tuesday and Thursday
    total_collected_dozens = collects_per_day * num_collection_days

    # L2
    delivered_to_market = 3 # delivers 3 dozen eggs to the market
    delivered_to_mall = 5 # delivers 5 dozen eggs to the mall
    total_sold_dozens = delivered_to_market + delivered_to_mall

    # L3
    remaining_dozens_after_sale = total_collected_dozens - total_sold_dozens

    # L4
    used_for_pie = 4 # uses 4 dozen eggs to make a pie
    remaining_dozens_after_pie = remaining_dozens_after_sale - used_for_pie

    # L5
    eggs_per_dozen = 12 # WK
    donated_eggs = remaining_dozens_after_pie * eggs_per_dozen

    # FA
    answer = donated_eggs
    return answer