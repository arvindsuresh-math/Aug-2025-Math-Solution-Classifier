def solve():
    """Index: 5964.
    Returns: the total money raised from the bake sale.
    """
    # L1
    betty_chocolate_chip_dozens = 4 # 4 dozen chocolate chip cookies
    betty_oatmeal_raisin_dozens = 6 # 6 dozen oatmeal raisin cookies
    paige_sugar_dozens = 6 # 6 dozen sugar cookies
    total_cookie_dozens = betty_chocolate_chip_dozens + betty_oatmeal_raisin_dozens + paige_sugar_dozens

    # L2
    dozen_size = 12 # WK
    total_cookies_count = dozen_size * total_cookie_dozens

    # L3
    betty_brownie_dozens = 2 # 2 dozen regular brownies
    paige_blondie_dozens = 3 # 3 dozen blondies
    paige_brownie_dozens = 5 # 5 dozen cream cheese swirled brownies
    total_brownie_dozens = betty_brownie_dozens + paige_blondie_dozens + paige_brownie_dozens

    # L4
    total_brownies_count = dozen_size * total_brownie_dozens

    # L5
    cookie_price_per_item = 1.00 # $1.00 apiece
    money_from_cookies = cookie_price_per_item * total_cookies_count

    # L6
    brownie_price_per_item = 2.00 # $2.00 apiece
    money_from_brownies = brownie_price_per_item * total_brownies_count

    # L7
    total_money_raised = money_from_cookies + money_from_brownies

    # FA
    answer = total_money_raised
    return answer