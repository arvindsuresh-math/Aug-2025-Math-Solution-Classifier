def solve(jolyn_therese_diff: int = 2, therese_aivo_diff: int = 5, leon_aivo_diff: int = 2) -> int:
    """
    Index: 85.
    Returns: the number of months Jolyn is older than Leon.
    """
    #: L1 Calculate how many months older Jolyn is compared to Aivo
    jolyn_aivo_diff = jolyn_therese_diff + therese_aivo_diff  # 2 + 5 = 7 months

    #: L2 Calculate how many months older Jolyn is compared to Leon
    answer = jolyn_aivo_diff - leon_aivo_diff  # 7 - 2 = 5 months # FINAL ANSWER
    return answer