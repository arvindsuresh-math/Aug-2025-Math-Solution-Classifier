def solve():
    """Index: 3486.
    Returns: the amount of money Randy had at first.
    """
    # L1
    money_left_after_giving_sally = 2000 # Randy has $2000 left
    gave_sally = 1200 # gave Sally $1,200
    money_before_giving_sally = money_left_after_giving_sally + gave_sally

    # L2
    smith_gave = 200 # Smith gave him another $200
    initial_money = money_before_giving_sally - smith_gave

    # FA
    answer = initial_money
    return answer