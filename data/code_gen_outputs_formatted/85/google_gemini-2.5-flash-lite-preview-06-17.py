def solve(
    j_t_diff: int = 2, # Jolyn is 2 months older than Therese
    t_a_diff: int = 5, # Therese is 5 months older than Aivo
    l_a_diff: int = 2 # Leon is 2 months older than Aivo
):
    """Index: 85.
    Returns: the age difference in months between Jolyn and Leon.
    """

    #: L1
    j_a_diff = j_t_diff + t_a_diff

    #: L2
    j_l_diff = j_a_diff - l_a_diff

    answer = j_l_diff # FINAL ANSWER
    return answer