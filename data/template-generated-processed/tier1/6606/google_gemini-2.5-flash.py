def solve():
    """Index: 6606.
    Returns: Umar's age.
    """
    # L1
    ali_age = 8 # Ali turned 8 years old this year
    ali_older_than_yusaf = 3 # 3 years older than Yusaf
    yusaf_age = ali_age - ali_older_than_yusaf

    # L2
    umar_multiplier = 2 # twice Yusaf’s age
    umar_age = yusaf_age * umar_multiplier

    # FA
    answer = umar_age
    return answer