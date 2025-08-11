def solve():
    """Index: 4925.
    Returns: the number of postcards Bernie has after all transactions.
    """
    # L1
    total_postcards = 18 # 18 unique postcards
    half_fraction = 0.5 # half his collection
    postcards_sold_count = total_postcards * half_fraction

    # L2
    price_per_postcard_sold = 15 # $15 per postcard
    money_earned = postcards_sold_count * price_per_postcard_sold

    # L3
    price_per_new_postcard = 5 # $5 each
    new_postcards_bought = money_earned / price_per_new_postcard

    # L4
    postcards_remaining_from_original = total_postcards - postcards_sold_count # The number of postcards Bernie kept from his original collection
    total_postcards_after_transactions = postcards_remaining_from_original + new_postcards_bought

    # FA
    answer = total_postcards_after_transactions
    return answer