def solve():
    """Index: 6468.
    Returns: the amount John spent on his phone.
    """
    # L1
    price_increase_percent = 2 # 2% more expensive
    alan_phone_price = 2000 # Alan bought a $2000 phone
    percent_factor = 0.01 # WK
    price_difference = price_increase_percent * percent_factor * alan_phone_price

    # L2
    john_phone_price = alan_phone_price + price_difference

    # FA
    answer = john_phone_price
    return answer