def solve():
    """Index: 3707.
    Returns: the average number of chocolate pieces per cookie.
    """
    # L1
    chocolate_chips = 108 # 108 chocolate chips
    m_and_m_ratio_denominator = 3 # one-third as many M&Ms
    m_and_m_ratio_numerator = 1 # one-third as many M&Ms
    total_m_and_ms = chocolate_chips / m_and_m_ratio_denominator / m_and_m_ratio_numerator

    # L2
    total_chocolate_pieces = total_m_and_ms + chocolate_chips

    # L3
    num_cookies = 48 # batch of 48 cookies
    average_pieces_per_cookie = total_chocolate_pieces / num_cookies

    # FA
    answer = average_pieces_per_cookie
    return answer