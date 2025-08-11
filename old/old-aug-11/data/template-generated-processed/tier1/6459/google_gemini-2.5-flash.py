def solve():
    """Index: 6459.
    Returns: the sum of Maggie's and Ralph's ages.
    """
    # L1
    juliet_age = 10 # Juliet is 10 years old
    juliet_older_than_maggie = 3 # Juliet is 3 years older than her sister Maggie
    maggie_age = juliet_age - juliet_older_than_maggie

    # L2
    juliet_younger_than_ralph = 2 # 2 years younger than her elder brother Ralph
    ralph_age = juliet_age + juliet_younger_than_ralph

    # L3
    sum_ages = maggie_age + ralph_age

    # FA
    answer = sum_ages
    return answer