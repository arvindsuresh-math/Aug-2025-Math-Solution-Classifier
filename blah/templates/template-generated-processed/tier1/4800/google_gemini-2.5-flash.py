def solve():
    """Index: 4800.
    Returns: the total amount of money Aliyah and Vivienne have together.
    """
    # L1
    vivienne_phones = 40 # Vivienne has 40 phones
    phone_price = 400 # sell their phones at $400 each
    vivienne_money = vivienne_phones * phone_price

    # L2
    aliyah_more_phones = 10 # Aliyah has 10 more phones
    aliyah_phones = vivienne_phones + aliyah_more_phones

    # L3
    aliyah_money = aliyah_phones * phone_price

    # L4
    total_money = aliyah_money + vivienne_money

    # FA
    answer = total_money
    return answer