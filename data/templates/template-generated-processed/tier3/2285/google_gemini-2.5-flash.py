from fractions import Fraction

def solve():
    """Index: 2285.
    Returns: the amount of money in the account before the transfer.
    """
    # L1
    transfer_to_mom = 60 # transferred $60 to her mom
    sister_fraction = Fraction(1, 2) # half that amount to her sister
    transfer_to_sister = transfer_to_mom * sister_fraction

    # L2
    total_transferred = transfer_to_mom + transfer_to_sister

    # L3
    remaining_money = 100 # her account now has $100 left in it
    initial_money = remaining_money + total_transferred

    # FA
    answer = initial_money
    return answer