def solve():
    """Index: 1841.
    Returns: the total dollars Mac lost.
    """
    # L1
    num_dimes_trade = 3 # trade him 3 dimes
    value_of_dime = 0.1 # WK
    value_three_dimes = num_dimes_trade * value_of_dime

    # L2
    num_nickels_trade = 7 # 7 nickels
    value_of_nickel = 0.05 # WK
    value_seven_nickels = num_nickels_trade * value_of_nickel

    # L3
    value_of_quarter = 0.25 # WK
    loss_per_dime_trade = value_three_dimes - value_of_quarter

    # L4
    loss_per_nickel_trade = value_seven_nickels - value_of_quarter

    # L5
    num_quarters_dimes = 20 # 20 quarters with dimes
    total_loss_dimes = num_quarters_dimes * loss_per_dime_trade

    # L6
    num_quarters_nickels = 20 # 20 quarters with nickels
    total_loss_nickels = num_quarters_nickels * loss_per_nickel_trade

    # L7
    total_loss = total_loss_dimes + total_loss_nickels

    # FA
    answer = total_loss
    return answer