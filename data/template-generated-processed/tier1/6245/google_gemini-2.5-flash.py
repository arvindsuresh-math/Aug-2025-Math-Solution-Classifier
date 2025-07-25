def solve():
    """Index: 6245.
    Returns: the total number of acorns they have altogether.
    """
    # L1
    shawna_acorns = 7 # Shawna has 7 acorns
    sheila_multiplier = 5 # 5 times as many acorns as Shawna
    sheila_acorns = shawna_acorns * sheila_multiplier

    # L2
    danny_fewer_than_sheila = 3 # 3 fewer acorns than Danny (meaning Danny has 3 more than Sheila)
    danny_acorns = sheila_acorns + danny_fewer_than_sheila

    # L3
    total_acorns = shawna_acorns + sheila_acorns + danny_acorns

    # FA
    answer = total_acorns
    return answer