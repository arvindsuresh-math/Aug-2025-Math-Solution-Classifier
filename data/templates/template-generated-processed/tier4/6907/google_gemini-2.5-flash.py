def solve():
    """Index: 6907.
    Returns: the total number of baths Bridgette gives in a year.
    """
    # L1
    dog_baths_per_month = 2 # She gives the dogs a bath twice a month
    months_per_year = 12 # WK
    dog_baths_per_year = dog_baths_per_month * months_per_year

    # L2
    cat_baths_per_month = 1 # She gives the cats a bath once a month
    cat_baths_per_year = cat_baths_per_month * months_per_year

    # L3
    bird_bath_frequency_numerator = 1 # She gives the birds a bath once every 4 months
    bird_bath_frequency_denominator = 4 # She gives the birds a bath once every 4 months
    bird_baths_per_month_avg = bird_bath_frequency_numerator / bird_bath_frequency_denominator

    # L4
    bird_baths_per_year = bird_baths_per_month_avg * months_per_year

    # L5
    num_dogs = 2 # 2 dogs
    total_dog_baths = num_dogs * dog_baths_per_year

    # L6
    num_cats = 3 # 3 cats
    total_cat_baths = num_cats * cat_baths_per_year

    # L7
    num_birds = 4 # 4 birds
    total_bird_baths = num_birds * bird_baths_per_year

    # L8
    total_baths_per_year = total_dog_baths + total_cat_baths + total_bird_baths

    # FA
    answer = total_baths_per_year
    return answer