def solve(
    clips_april: int = 48, # Natalia sold clips to 48 of her friends in April
    fraction_may_sales: float = 0.5 # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May.
    """

    #: L1
    clips_may = clips_april * fraction_may_sales # eval: 24.0 = 48 * 0.5

    #: L2
    total_clips = 82.0 # eval: 82.0 = 82.0

    #: FA
    answer = total_clips
    return answer # eval: return 82.0
