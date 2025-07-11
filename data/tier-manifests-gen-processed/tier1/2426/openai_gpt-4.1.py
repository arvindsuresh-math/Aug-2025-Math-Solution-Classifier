def solve():
    """Index: 2426.
    Returns: the total scholarship money received by Wendy, Kelly, and Nina together.
    """
    # L1
    wendy_scholarship = 20000 # Wendy received a scholarship worth $20000
    kelly_multiplier = 2 # Kelly received a scholarship worth twice the amount Wendy received
    kelly_scholarship = kelly_multiplier * wendy_scholarship

    # L2
    wendy_and_kelly = kelly_scholarship + wendy_scholarship

    # L3
    nina_less_than_kelly = 8000 # Nina has received a scholarship worth $8000 less than Kelly's amount
    nina_scholarship = kelly_scholarship - nina_less_than_kelly

    # L4
    total_scholarship = nina_scholarship + wendy_and_kelly

    # FA
    answer = total_scholarship
    return answer