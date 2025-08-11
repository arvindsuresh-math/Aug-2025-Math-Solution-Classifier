def solve():
    """Index: 4478.
    Returns: the amount of dollars each girl will get after paying off the debt.
    """
    # L1
    lulu_savings = 6 # Lulu has saved $6
    nora_multiplier = 5 # Nora has saved five times what Lulu has
    nora_savings = nora_multiplier * lulu_savings

    # L2
    tamara_divisor = 3 # three times Tamara’s savings
    tamara_savings = nora_savings / tamara_divisor

    # L3
    total_savings = nora_savings + tamara_savings + lulu_savings

    # L4
    debt_amount = 40 # pay off a $40 debt
    remaining_money_after_debt = total_savings - debt_amount

    # L5
    number_of_girls = 3 # Tamara, Nora, and Lulu
    money_per_girl = remaining_money_after_debt / number_of_girls

    # FA
    answer = money_per_girl
    return answer