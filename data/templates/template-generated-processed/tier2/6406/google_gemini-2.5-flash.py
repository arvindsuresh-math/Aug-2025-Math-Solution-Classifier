def solve():
    """Index: 6406.
    Returns: the total money Enrico was able to earn from selling roosters.
    """
    # L1
    rooster_1_weight = 30 # a 30-kilogram rooster
    price_per_kg = 0.50 # $0.50 per kilogram
    rooster_1_price = rooster_1_weight * price_per_kg

    # L2
    rooster_2_weight = 40 # a 40-kilogram rooster
    rooster_2_price = rooster_2_weight * price_per_kg

    # L3
    total_earnings = rooster_2_price + rooster_1_price

    # FA
    answer = total_earnings
    return answer