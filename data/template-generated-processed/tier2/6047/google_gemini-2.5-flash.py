def solve():
    """Index: 6047.
    Returns: the total money Kyle will make from selling his baked goods.
    """
    # L1
    kyle_eats_cookies = 2 # Kyle eats 2 cookies
    mom_eats_cookies = 1 # Kyle's mom eats 1 cookie
    total_cookies_eaten = kyle_eats_cookies + mom_eats_cookies

    # L2
    kyle_eats_brownies = 2 # Kyle eats 2 brownies
    mom_eats_brownies = 2 # Kyle's mom eats 2 brownies
    total_brownies_eaten = kyle_eats_brownies + mom_eats_brownies

    # L3
    initial_cookies = 60 # Kyle bakes 60 cookies
    remaining_cookies = initial_cookies - total_cookies_eaten

    # L4
    initial_brownies = 32 # 32 brownies
    remaining_brownies = initial_brownies - total_brownies_eaten

    # L5
    cookie_price = 1 # a cookie for $1
    money_from_cookies = remaining_cookies * cookie_price

    # L6
    brownie_price = 1.50 # a brownie for $1.50
    money_from_brownies = remaining_brownies * brownie_price

    # L7
    total_money = money_from_cookies + money_from_brownies

    # FA
    answer = total_money
    return answer