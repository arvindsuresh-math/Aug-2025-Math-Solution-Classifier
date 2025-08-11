def solve():
    """Index: 7397.
    Returns: the number of people Ryan needs to recruit.
    """
    # L1
    target_fund = 1000 # a $1,000 business
    cash_on_hand = 200 # he has $200 already
    money_needed = target_fund - cash_on_hand

    # L2
    contribution_per_person = 10 # average person funds $10
    people_to_recruit = money_needed / contribution_per_person

    # FA
    answer = people_to_recruit
    return answer