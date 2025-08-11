def solve():
    """Index: 6527.
    Returns: the total amount of money Cathy has now.
    """
    # L1
    initial_money = 12 # Cathy has $12 left in her wallet
    dad_sent = 25 # her dad sent her $25
    money_after_dad = initial_money + dad_sent

    # L2
    multiplier_mom = 2 # twice the amount her dad sent her
    mom_sent = dad_sent * multiplier_mom

    # L3
    total_money = mom_sent + money_after_dad

    # FA
    answer = total_money
    return answer