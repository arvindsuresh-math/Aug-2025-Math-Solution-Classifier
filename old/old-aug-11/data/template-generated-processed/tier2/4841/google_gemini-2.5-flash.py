def solve():
    """Index: 4841.
    Returns: the number of men with beards who have been Scrabble champion.
    """
    # L1
    total_percentage = 100 # WK
    women_champion_percentage = 60 # 60% of Scrabble champions have been women
    men_champion_percentage = total_percentage - women_champion_percentage

    # L2
    total_champions_years = 25 # In the last 25 years
    men_percent_as_decimal = 0.4 # derived from "60% of Scrabble champions have been women and the rest have been men"
    num_men_champions = total_champions_years * men_percent_as_decimal

    # L3
    beard_percent_as_decimal = 0.4 # 40% had a beard
    num_men_with_beards = num_men_champions * beard_percent_as_decimal

    # FA
    answer = num_men_with_beards
    return answer