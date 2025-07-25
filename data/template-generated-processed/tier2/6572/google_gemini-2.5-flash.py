def solve():
    """Index: 6572.
    Returns: how much money Josh has left.
    """
    # L1
    initial_money = 20 # Josh’s mom gives him $20
    hat_cost = 10 # buys a hat for $10
    money_after_hat = initial_money - hat_cost

    # L2
    pencil_cost = 2 # a pencil for $2
    money_after_pencil = money_after_hat - pencil_cost

    # L3
    num_cookies = 4 # four cookies
    cookie_cost_per_item = 1.25 # each cookie costs $1.25
    total_cookie_cost = num_cookies * cookie_cost_per_item

    # L4
    money_left = money_after_pencil - total_cookie_cost

    # FA
    answer = money_left
    return answer