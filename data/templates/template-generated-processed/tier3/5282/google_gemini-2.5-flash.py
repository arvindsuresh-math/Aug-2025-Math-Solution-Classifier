from fractions import Fraction

def solve():
    """Index: 5282.
    Returns: the number of dollars Willie gets.
    """
    # L1
    euros_willie_has = 70 # 70 euros
    official_exchange_rate_euros_per_dollar = 5 # 5 euros is worth 1 dollar
    dollars_at_official_rate = euros_willie_has / official_exchange_rate_euros_per_dollar

    # L2
    airport_exchange_numerator = 5 # 5/7ths of the official exchange rate
    airport_exchange_denominator = 7 # 5/7ths of the official exchange rate
    # airport_exchange_fraction = Fraction(airport_exchange_numerator, airport_exchange_denominator) # This variable is not directly substituted into the template
    dollars_at_official_rate_divided_by_denominator = dollars_at_official_rate / airport_exchange_denominator
    dollars_willie_gets = dollars_at_official_rate_divided_by_denominator * airport_exchange_numerator

    # FA
    answer = dollars_willie_gets
    return answer