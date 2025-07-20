def solve():
    """Index: 5570.
    Returns: the total amount Lowry earned.
    """
    # L1
    small_bonsai_cost = 30 # A small bonsai costs $30
    num_small_bonsai = 3 # sold 3 small bonsai
    earnings_small_bonsai = small_bonsai_cost * num_small_bonsai

    # L2
    big_bonsai_cost = 20 # a big bonsai costs $20
    num_big_bonsai = 5 # sold 5 big bonsai
    earnings_big_bonsai = big_bonsai_cost * num_big_bonsai

    # L3
    total_earnings = earnings_big_bonsai + earnings_small_bonsai

    # FA
    answer = total_earnings
    return answer