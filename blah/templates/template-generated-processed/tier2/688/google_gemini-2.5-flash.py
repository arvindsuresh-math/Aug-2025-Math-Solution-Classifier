def solve():
    """Index: 688.
    Returns: the number of tadpoles Trent kept.
    """
    # L1
    total_tadpoles = 180 # 180 tadpoles
    released_percentage_decimal = 0.75 # 75% of them go
    released_tadpoles = total_tadpoles * released_percentage_decimal

    # L2
    kept_tadpoles = total_tadpoles - released_tadpoles

    # FA
    answer = kept_tadpoles
    return answer