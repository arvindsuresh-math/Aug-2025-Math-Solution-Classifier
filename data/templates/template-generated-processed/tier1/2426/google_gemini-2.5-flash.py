def solve():
    """Index: 2426.
    Returns: the total scholarship amount received by Nina, Kelly, and Wendy.
    """
    # L1
    wendy_scholarship = 20000 # Wendy received a scholarship worth $20000
    multiplier_for_twice = 2 # twice the amount Wendy received
    kelly_scholarship = multiplier_for_twice * wendy_scholarship

    # L2
    wendy_kelly_total = kelly_scholarship + wendy_scholarship

    # L3
    nina_less_than_kelly = 8000 # $8000 less than Kelly's amount
    nina_scholarship = kelly_scholarship - nina_less_than_kelly

    # L4
    total_scholarship = nina_scholarship + wendy_kelly_total

    # FA
    answer = total_scholarship
    return answer