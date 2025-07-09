def solve(
    clips_april: int = 48, # Natalia sold clips to 48 of her friends in April
    fraction_may_sales: float = 0.5 # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May.
    """

    #: L1
    clips_may = clips_april * clips_april # eval: 2304 = 48 * 48

    #: L2
    total_clips = clips_april + clips_may # eval: 2352 = 48 + 2304

    #: FA
    answer = total_clips
    return answer # eval: return 2352
