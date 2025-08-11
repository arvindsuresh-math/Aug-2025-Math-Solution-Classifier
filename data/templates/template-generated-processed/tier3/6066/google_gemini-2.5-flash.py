from fractions import Fraction

def solve():
    """Index: 6066.
    Returns: the total amount Alan will have to pay for all the products.
    """
    # L1
    avn_cd_price = 12 # The price of the "AVN" CD is $12
    dark_cd_price_multiplier = 2 # half the price of one CD by "The Dark"
    dark_cd_price = avn_cd_price * dark_cd_price_multiplier

    # L2
    num_dark_cds = 2 # buy 2 CDs by "The Dark"
    total_dark_cds_cost = dark_cd_price * num_dark_cds

    # L3
    cost_of_other_cds = avn_cd_price + total_dark_cds_cost

    # L4
    nineties_music_percentage = Fraction(40, 100) # 40% of all the cost of all other CDs
    nineties_music_cds_cost = nineties_music_percentage * cost_of_other_cds

    # L5
    total_cost = cost_of_other_cds + nineties_music_cds_cost

    # FA
    answer = total_cost
    return answer