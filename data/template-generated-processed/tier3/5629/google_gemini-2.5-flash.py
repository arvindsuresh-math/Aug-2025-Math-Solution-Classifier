from fractions import Fraction

def solve():
    """Index: 5629.
    Returns: the percentage of the town that is immune in some way.
    """
    # L1
    vaccinated_fraction = Fraction(1, 3) # 1/3 of the townspeople have received the full COVID vaccine
    recovered_fraction = Fraction(1, 3) # 1/3 are immune because they already recovered from COVID
    sum_vaccinated_recovered = vaccinated_fraction + recovered_fraction

    # L2
    both_vaccinated_recovered_fraction = Fraction(1, 6) # 1/6 of the townspeople are both vaccinated and already had COVID
    conversion_numerator = 2 # WK
    conversion_denominator = 2 # WK
    sum_vaccinated_recovered_common_denominator = sum_vaccinated_recovered * Fraction(conversion_numerator, conversion_denominator)

    # L3
    total_immune_fraction = sum_vaccinated_recovered_common_denominator - both_vaccinated_recovered_fraction

    # L4
    percentage_multiplier = 100 # WK
    immune_percentage = float(total_immune_fraction) * percentage_multiplier

    # FA
    answer = immune_percentage
    return answer