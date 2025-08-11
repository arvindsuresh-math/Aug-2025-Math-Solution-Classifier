def solve():
    """Index: 3327.
    Returns: the total number of gems Tom ended up with.
    """
    # L1
    money_spent = 250 # Tom spends $250
    gems_per_dollar = 100 # 100 gems for each dollar
    initial_gems = money_spent * gems_per_dollar

    # L2
    bonus_percent = 0.2 # 20% bonus
    bonus_gems = initial_gems * bonus_percent

    # L3
    total_gems = initial_gems + bonus_gems

    # FA
    answer = total_gems
    return answer