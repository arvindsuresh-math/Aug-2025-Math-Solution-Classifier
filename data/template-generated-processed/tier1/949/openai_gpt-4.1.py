def solve():
    """Index: 949.
    Returns: how much Yola weighed 2 years ago.
    """
    # L1
    yola_current = 220 # Yola currently weighs 220 pounds
    wanda_more_than_yola = 30 # Wanda weighs 30 pounds more than Yola
    wanda_current = yola_current + wanda_more_than_yola

    # L2
    wanda_more_than_yola_2yrs_ago = 80 # Wanda weighs 80 pounds more than Yola did 2 years ago
    yola_2yrs_ago = wanda_current - wanda_more_than_yola_2yrs_ago

    # FA
    answer = yola_2yrs_ago
    return answer