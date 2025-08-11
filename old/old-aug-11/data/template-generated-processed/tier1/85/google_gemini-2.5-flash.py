def solve():
    """Index: 85.
    Returns: how much older in months Jolyn is than Leon.
    """
    # L1
    jolyn_older_than_therese = 2 # 2 months older than Therese
    therese_older_than_aivo = 5 # 5 months older than Aivo
    jolyn_older_than_aivo = jolyn_older_than_therese + therese_older_than_aivo

    # L2
    leon_older_than_aivo = 2 # 2 months older than Aivo
    jolyn_older_than_leon = jolyn_older_than_aivo - leon_older_than_aivo

    # FA
    answer = jolyn_older_than_leon
    return answer