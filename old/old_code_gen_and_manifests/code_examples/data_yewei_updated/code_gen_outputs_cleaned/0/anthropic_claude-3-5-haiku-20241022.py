def solve(
    clips_sold_in_april: int = 48,  # Natalia sold clips to 48 of her friends in April
    fraction_of_april_sales: float = 1/2  # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May."""
    #: L1
    clips_sold_in_may = clips_sold_in_april * fraction_of_april_sales

    #: L2
    total_clips_sold = clips_sold_in_april + clips_sold_in_may

    answer = total_clips_sold  # FINAL ANSWER
    return answer