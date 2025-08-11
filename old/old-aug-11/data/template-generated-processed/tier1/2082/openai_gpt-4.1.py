def solve():
    """Index: 2082.
    Returns: the amount of money left after Mildred and Candice spent their money.
    """
    # L1
    mildred_spent = 25 # Mildred spent $25
    candice_spent = 35 # Candice spent $35
    total_spent = mildred_spent + candice_spent

    # L2
    mom_gave = 100 # their mom gave them $100 to spend
    money_left = mom_gave - total_spent

    # FA
    answer = money_left
    return answer