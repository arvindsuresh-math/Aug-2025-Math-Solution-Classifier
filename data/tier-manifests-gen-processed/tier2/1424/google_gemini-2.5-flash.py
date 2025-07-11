def solve():
    """Index: 1424.
    Returns: how much more money Christian and Sue need to make.
    """
    # L1
    yards_mowed_christian = 4 # mowed 4 of his neighbors' yards
    charge_per_yard = 5.00 # charging $5.00 each
    christian_earnings_mowing = yards_mowed_christian * charge_per_yard

    # L2
    dogs_walked_sue = 6 # walked 6 dogs
    charge_per_dog = 2.00 # charging $2.00 per dog
    sue_earnings_walking = dogs_walked_sue * charge_per_dog

    # L3
    christian_saved = 5.00 # Christian had $5.00 saved up
    sue_saved = 7.00 # Sue had $7.00
    total_money_combined = christian_saved + christian_earnings_mowing + sue_saved + sue_earnings_walking

    # L4
    perfume_cost = 50.00 # $50.00 bottle of perfume
    money_needed = perfume_cost - total_money_combined

    # FA
    answer = money_needed
    return answer