def solve():
    """Index: 6672.
    Returns: the number of weeks Patty can go without doing chores.
    """
    # L1
    total_money = 15 # Patty has $15
    cost_per_pack = 3 # Each pack of cookies ... costs $3
    packs_of_cookies = total_money / cost_per_pack

    # L2
    cookies_per_pack = 24 # Each pack of cookies contains 24 cookies
    total_cookies = packs_of_cookies * cookies_per_pack

    # L3
    cookies_per_chore = 3 # 3 cookies for every chore
    chores_per_kid_per_week = 4 # Each kid normally has 4 chores to do per week
    weekly_cookie_cost = cookies_per_chore * chores_per_kid_per_week

    # L4
    weeks_without_chores = total_cookies / weekly_cookie_cost

    # FA
    answer = weeks_without_chores
    return answer