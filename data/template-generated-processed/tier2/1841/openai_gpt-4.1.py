def solve():
    """Index: 1841.
    Returns: the total number of dollars Mac lost in the trades.
    """
    # L1
    dimes_per_trade = 3 # trade him 3 dimes for a quarter
    dime_value = 0.1 # value of a dime is $0.1
    dimes_trade_value = dimes_per_trade * dime_value

    # L2
    nickels_per_trade = 7 # or 7 nickels
    nickel_value = 0.05 # value of a nickel is $0.05
    nickels_trade_value = nickels_per_trade * nickel_value

    # L3
    quarter_value = 0.25 # value of a quarter is $0.25
    loss_per_dime_trade = dimes_trade_value - quarter_value

    # L4
    loss_per_nickel_trade = nickels_trade_value - quarter_value

    # L5
    num_dime_trades = 20 # trades for 20 quarters with dimes
    total_loss_dimes = num_dime_trades * loss_per_dime_trade

    # L6
    num_nickel_trades = 20 # trades for 20 quarters with nickels
    total_loss_nickels = num_nickel_trades * loss_per_nickel_trade

    # L7
    total_loss = total_loss_dimes + total_loss_nickels

    # FA
    answer = total_loss
    return answer