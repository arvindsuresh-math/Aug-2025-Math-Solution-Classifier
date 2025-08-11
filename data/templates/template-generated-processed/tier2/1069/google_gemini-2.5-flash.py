def solve():
    """Index: 1069.
    Returns: the total amount of money Maria has in dollars.
    """
    # L1
    initial_quarters = 4 # 4 quarters
    mom_gives_quarters = 5 # her mom gives her 5 quarters
    total_quarters = initial_quarters + mom_gives_quarters

    # L2
    value_of_quarter = 0.25 # WK
    dollars_from_quarters = total_quarters * value_of_quarter

    # L3
    num_dimes = 4 # 4 dimes
    value_of_dime = 0.10 # WK
    dollars_from_dimes = num_dimes * value_of_dime

    # L4
    num_nickels = 7 # 7 nickels
    value_of_nickel = 0.05 # WK
    dollars_from_nickels = num_nickels * value_of_nickel

    # L5
    total_dollars = dollars_from_quarters + dollars_from_dimes + dollars_from_nickels

    # FA
    answer = total_dollars
    return answer