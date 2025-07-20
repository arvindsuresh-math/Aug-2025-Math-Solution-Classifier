def solve():
    """Index: 6082.
    Returns: the total number of cookies these three boys have.
    """
    # L1
    glenn_cookies = 24 # Glenn has 24 cookies
    glenn_multiplier = 4 # Glenn has four times as many cookies as Kenny
    kenny_cookies = glenn_cookies / glenn_multiplier

    # L2
    chris_divisor = 2 # Chris has half as many cookies as Kenny
    chris_cookies = kenny_cookies / chris_divisor

    # L3
    total_cookies = glenn_cookies + kenny_cookies + chris_cookies

    # FA
    answer = total_cookies
    return answer