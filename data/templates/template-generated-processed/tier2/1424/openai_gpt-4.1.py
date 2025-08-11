def solve():
    """Index: 1424.
    Returns: the additional amount Christian and Sue need to make to buy the perfume.
    """
    # L1
    christian_yards = 4 # mowed 4 of his neighbors' yards
    christian_yard_rate = 5.00 # charging $5.00 each
    christian_earned = christian_yards * christian_yard_rate

    # L2
    sue_dogs = 6 # walked 6 dogs
    sue_dog_rate = 2.00 # charging $2.00 per dog
    sue_earned = sue_dogs * sue_dog_rate

    # L3
    christian_saved = 5.00 # Christian had $5.00 saved up
    sue_saved = 7.00 # Sue had $7.00
    total_money = christian_saved + christian_earned + sue_saved + sue_earned

    # L4
    perfume_cost = 50.00 # $50.00 bottle of perfume
    additional_needed = perfume_cost - total_money

    # FA
    answer = additional_needed
    return answer