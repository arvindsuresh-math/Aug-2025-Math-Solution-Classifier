from fractions import Fraction

def solve():
    """Index: 1824.
    Returns: the total number of food items donated by the companies.
    """
    # L1
    foster_farms_chicken = 45 # Foster Farms donated 45 dressed chickens
    american_summits_multiplier = 2 # twice the number of bottled water
    american_summits_water = foster_farms_chicken * american_summits_multiplier

    # L2
    hormel_multiplier = 3 # three times the number of dressed chickens
    hormel_spams = foster_farms_chicken * hormel_multiplier

    # L3
    boudin_fraction = Fraction(1, 3) # one-third of the number
    boudin_sourdoughs = hormel_spams * boudin_fraction

    # L4
    del_monte_difference = 30 # 30 fewer bottles of water
    del_monte_canned_fruits = american_summits_water - del_monte_difference

    # L5
    total_food_items = foster_farms_chicken + american_summits_water + hormel_spams + boudin_sourdoughs + del_monte_canned_fruits

    # FA
    answer = total_food_items
    return answer