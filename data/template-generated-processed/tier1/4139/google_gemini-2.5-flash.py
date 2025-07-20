def solve():
    """Index: 4139.
    Returns: the total number of ninja throwing stars they have altogether.
    """
    # L1
    eric_stars = 4 # Eric has 4 ninja throwing stars
    chad_multiplier = 2 # twice as many
    chad_stars_initial = eric_stars * chad_multiplier

    # L2
    stars_sold_to_jeff = 2 # bought 2 ninja stars from Chad
    chad_stars_after_sale = chad_stars_initial - stars_sold_to_jeff

    # L3
    jeff_stars_final = 6 # Jeff now has 6 throwing stars
    total_stars = eric_stars + chad_stars_after_sale + jeff_stars_final

    # FA
    answer = total_stars
    return answer