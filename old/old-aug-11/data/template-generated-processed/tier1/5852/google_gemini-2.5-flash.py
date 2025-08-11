def solve():
    """Index: 5852.
    Returns: the amount of money Lidia will be left with after buying all apps.
    """
    # L1
    app_cost = 4 # One app costs $4
    num_apps = 15 # needs 15 of them
    total_app_cost = app_cost * num_apps

    # L2
    initial_money = 66 # She has $66 for this purpose
    money_left = initial_money - total_app_cost

    # FA
    answer = money_left
    return answer