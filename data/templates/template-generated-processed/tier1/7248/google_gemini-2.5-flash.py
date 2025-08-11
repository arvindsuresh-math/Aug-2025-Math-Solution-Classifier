def solve():
    """Index: 7248.
    Returns: the amount of money Mikail's parents will give him.
    """
    # L1
    times_older = 3 # 3 times older
    age_when_three = 3 # when he was three
    mikail_current_age = times_older * age_when_three

    # L2
    money_per_year = 5 # $5 for every year old he is
    total_money = mikail_current_age * money_per_year

    # FA
    answer = total_money
    return answer