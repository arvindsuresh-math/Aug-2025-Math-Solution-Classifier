def solve(
    months_older_jolyn_therese: int = 2, # Jolyn is 2 months older than Therese
    months_older_therese_aivo: int = 5, # Therese is 5 months older than Aivo
    months_older_leon_aivo: int = 2 # Leon is 2 months older than Aivo
):
    """Index: 85.
    Returns: the difference in months between Jolyn's and Leon's ages.
    """
    #: L1
    months_older_jolyn_aivo = months_older_jolyn_therese + months_older_therese_aivo

    #: L2
    difference_jolyn_leon = months_older_jolyn_aivo - months_older_leon_aivo

    answer = difference_jolyn_leon # FINAL ANSWER
    return answer