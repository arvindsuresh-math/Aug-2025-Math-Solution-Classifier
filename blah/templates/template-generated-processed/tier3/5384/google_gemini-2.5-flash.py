from fractions import Fraction

def solve():
    """Index: 5384.
    Returns: the total number of fruits the apple tree grew in the three seasons.
    """
    # L1
    first_season_apples = 200 # produced 200 apples in a particular season
    reduction_percentage = Fraction(20, 100) # 20% fewer fruits
    fewer_fruits_second_season = reduction_percentage * first_season_apples

    # L2
    second_season_apples = first_season_apples - fewer_fruits_second_season

    # L3
    total_fruits_first_two_seasons = second_season_apples + first_season_apples

    # L4
    doubling_factor = 2 # doubled during the third season
    third_season_apples = second_season_apples * doubling_factor

    # L5
    total_fruits_three_seasons = third_season_apples + total_fruits_first_two_seasons

    # FA
    answer = total_fruits_three_seasons
    return answer