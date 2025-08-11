def solve():
    """Index: 1835.
    Returns: the total money saved by the three kids.
    """
    # L1
    teagan_pennies_count = 200 # 200 pennies
    penny_value_cents = 1 # WK
    penny_value_decimal = 0.01 # WK
    teagan_total_money = penny_value_decimal * teagan_pennies_count

    # L2
    rex_nickels_count = 100 # 100 nickels
    nickel_value_cents = 5 # WK
    nickel_value_decimal = 0.05 # WK
    rex_total_money = nickel_value_decimal * rex_nickels_count

    # L3
    toni_dimes_count = 330 # 330 dimes
    dime_value_cents = 10 # WK
    dime_value_decimal = 0.10 # WK
    toni_total_money = dime_value_decimal * toni_dimes_count

    # L4
    total_money_saved = teagan_total_money + rex_total_money + toni_total_money

    # FA
    answer = total_money_saved
    return answer