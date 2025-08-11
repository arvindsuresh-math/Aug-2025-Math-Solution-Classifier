def solve():
    """Index: 2082.
    Returns: the amount of money left after spending.
    """
    # L1
    mildred_spent = 25 # Mildred spent $25
    candice_spent = 35 # Candice spent $35
    total_spent = mildred_spent + candice_spent

    # L2
    initial_money = 100 # mom gave them $100
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer