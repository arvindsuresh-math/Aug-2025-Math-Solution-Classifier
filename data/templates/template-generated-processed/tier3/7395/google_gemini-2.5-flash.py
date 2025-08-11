def solve():
    """Index: 7395.
    Returns: the number of jellybeans Matilda has.
    """
    # L1
    steve_jellybeans = 84 # Steve has 84 jellybeans
    matt_multiplier = 10 # ten times as many jellybeans as Steve
    matt_jellybeans = steve_jellybeans * matt_multiplier

    # L2
    matilda_divisor = 2 # half as many jellybeans as Matt
    matilda_jellybeans = matt_jellybeans / matilda_divisor

    # FA
    answer = matilda_jellybeans
    return answer