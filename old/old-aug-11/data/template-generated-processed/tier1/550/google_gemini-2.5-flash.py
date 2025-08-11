def solve():
    """Index: 550.
    Returns: the value, in dollars, of the rest of the money Randy kept.
    """
    # L1
    randy_initial_money = 3000 # Randy had $3,000
    smith_gave = 200 # Smith gave him another $200
    randy_money_after_smith = randy_initial_money + smith_gave

    # L2
    sally_received = 1200 # Randy then gave Sally $1,200
    money_kept = randy_money_after_smith - sally_received

    # FA
    answer = money_kept
    return answer