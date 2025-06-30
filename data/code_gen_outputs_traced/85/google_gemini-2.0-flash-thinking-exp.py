def solve(
    jolyn_older_than_therese: int = 2, # Jolyn is 2 months older than Therese
    therese_older_than_aivo: int = 5, # Therese is 5 months older than Aivo
    leon_older_than_aivo: int = 2 # Leon is 2 months older than Aivo
):
    """Index: 85.
    Returns: the age difference in months between Jolyn and Leon.
    """

    #: L1
    jolyn_older_than_aivo = jolyn_older_than_therese + therese_older_than_aivo # eval: 7 = 2 + 5

    #: L2
    jolyn_older_than_leon = jolyn_older_than_aivo - leon_older_than_aivo # eval: 5 = 7 - 2

    #: FA
    answer = jolyn_older_than_leon # eval: 5 = 5
    return answer # eval: return 5
