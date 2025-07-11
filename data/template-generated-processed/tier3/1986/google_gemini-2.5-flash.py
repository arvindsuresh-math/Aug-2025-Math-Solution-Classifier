def solve():
    """Index: 1986.
    Returns: the amount of money Samuel has left.
    """
    # L1
    total_money = 240 # $240 was divided between Kelvin and Samuel
    samuel_fraction_numerator = 3 # Samuel received 3/4 of the money
    samuel_fraction_denominator = 4 # Samuel received 3/4 of the money
    samuel_share = total_money * samuel_fraction_numerator / samuel_fraction_denominator

    # L2
    spent_fraction_numerator = 1 # spent 1/5 of the original $240
    spent_fraction_denominator = 5 # spent 1/5 of the original $240
    spent_on_drinks = total_money * spent_fraction_numerator / spent_fraction_denominator

    # L3
    samuel_left = samuel_share - spent_on_drinks

    # FA
    answer = samuel_left
    return answer