def solve():
    """Index: 1835.
    Returns: the total amount of money the three kids saved altogether.
    """
    # L1
    penny_value = 0.01 # 1 cent (.01)
    teagan_pennies = 200 # Teagan saved 200 pennies
    teagan_amount = penny_value * teagan_pennies

    # L2
    nickel_value = 0.05 # 5 cents (.05)
    rex_nickels = 100 # Rex has 100 nickels
    rex_amount = nickel_value * rex_nickels

    # L3
    dime_value = 0.10 # 10 cents (.10)
    toni_dimes = 330 # Toni has 330 dimes
    toni_amount = dime_value * toni_dimes

    # L4
    total_amount = teagan_amount + rex_amount + toni_amount

    # FA
    answer = total_amount
    return answer