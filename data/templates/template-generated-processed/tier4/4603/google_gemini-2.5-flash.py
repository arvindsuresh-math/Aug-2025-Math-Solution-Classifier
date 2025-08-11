def solve():
    """Index: 4603.
    Returns: the percentage of remaining cats that are kittens, rounded to the nearest percent.
    """
    # L1
    total_cats = 6 # Matt has six cats
    female_cat_fraction_divisor = 2 # half of them are female
    female_cats = total_cats / female_cat_fraction_divisor

    # L2
    kittens_per_female_cat = 7 # each female cat has 7 kittens
    total_kittens_born = kittens_per_female_cat * female_cats

    # L3
    kittens_sold = 9 # Matt sells 9 of them
    remaining_kittens = total_kittens_born - kittens_sold

    # L4
    total_cats_after_sale = remaining_kittens + total_cats

    # L5
    percent_multiplier = 100 # WK
    percentage_kittens_raw = (remaining_kittens / total_cats_after_sale) * percent_multiplier
    percentage_kittens = round(percentage_kittens_raw)

    # FA
    answer = percentage_kittens
    return answer