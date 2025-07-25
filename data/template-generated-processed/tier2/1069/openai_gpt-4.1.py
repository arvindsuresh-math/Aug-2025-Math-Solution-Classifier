def solve():
    """Index: 1069.
    Returns: the total amount of money Maria has now, in dollars.
    """
    # L1
    original_quarters = 4 # Maria has 4 quarters
    quarters_given = 5 # Her mom gives her 5 quarters
    total_quarters = original_quarters + quarters_given

    # L2
    quarter_value = 0.25 # $0.25 per quarter
    dollars_from_quarters = total_quarters * quarter_value

    # L3
    num_dimes = 4 # Maria has 4 dimes
    dime_value = 0.10 # $0.10 per dime
    dollars_from_dimes = num_dimes * dime_value

    # L4
    num_nickels = 7 # Maria has 7 nickels
    nickel_value = 0.05 # $0.05 per nickel
    dollars_from_nickels = num_nickels * nickel_value

    # L5
    total_dollars = dollars_from_quarters + dollars_from_dimes + dollars_from_nickels

    # FA
    answer = total_dollars
    return answer