def solve(
    clips_sold_april: int = 48  # Natalia sold clips to 48 of her friends in April
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May.
    """

    #: L1
    clips_sold_may = clips_sold_april / 2 # eval: 24.0 = 48 / 2

    #: L2
    total_clips_sold = clips_sold_april - clips_sold_may # eval: 24.0 = 48 - 24.0

    #: FA
    answer = total_clips_sold
    return answer # eval: return 24.0
