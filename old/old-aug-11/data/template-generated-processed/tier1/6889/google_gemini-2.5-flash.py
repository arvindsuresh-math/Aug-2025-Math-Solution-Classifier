def solve():
    """Index: 6889.
    Returns: the amount of money Mr. Ben is remaining with.
    """
    # L1
    initial_money = 2000 # Ben has $2000 for his business operations costs
    cheque_amount = 600 # writes them a cheque for $600
    money_after_cheque = initial_money - cheque_amount

    # L2
    debtor_payment = 800 # debtor pays him $800
    money_after_debtor_payment = money_after_cheque + debtor_payment

    # L3
    maintenance_cost = 1200 # spends $1200 on the whole operation
    money_after_maintenance = money_after_debtor_payment - maintenance_cost

    # FA
    answer = money_after_maintenance
    return answer