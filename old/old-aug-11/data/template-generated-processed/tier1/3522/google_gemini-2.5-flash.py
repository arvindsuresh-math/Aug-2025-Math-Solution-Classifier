def solve():
    """Index: 3522.
    Returns: the total money saved for holiday spending.
    """
    # L1
    sam_saves = 1000 # Sam saves $1000
    victory_less_than_sam = 100 # Victory saves $100 less than Sam
    victory_saves = sam_saves - victory_less_than_sam

    # L2
    total_money_saved = sam_saves + victory_saves

    # FA
    answer = total_money_saved
    return answer