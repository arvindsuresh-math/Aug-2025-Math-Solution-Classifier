from fractions import Fraction

def solve():
    """Index: 3255.
    Returns: the total number of people at the concert.
    """
    # L1
    total_percentage = 100 # WK
    women_percentage = 60 # 60% are women
    men_percentage = total_percentage - women_percentage

    # L2
    num_men = 20 # there are 20 men
    percent_to_decimal_divisor = 100 # WK
    men_percentage_decimal = men_percentage / percent_to_decimal_divisor
    under_30_second_band_total = num_men / men_percentage_decimal

    # L3
    under_30_percent_second_band = 50 # 50% of the audience there for the second band is under the age of 30
    under_30_percent_second_band_decimal = under_30_percent_second_band / percent_to_decimal_divisor
    second_band_audience_total = under_30_second_band_total / under_30_percent_second_band_decimal

    # L4
    second_band_fraction = Fraction(2, 3) # 2/3 of the audience was there for the second band
    total_concert_people = second_band_audience_total / second_band_fraction

    # FA
    answer = total_concert_people
    return answer