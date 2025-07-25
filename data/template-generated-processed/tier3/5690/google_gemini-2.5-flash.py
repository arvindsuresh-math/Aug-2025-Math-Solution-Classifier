from fractions import Fraction

def solve():
    """Index: 5690.
    Returns: 40% of Jacqueline's candy bars.
    """
    # L1
    fred_candy_bars = 12 # Fred has 12 identical candy bars
    bob_more_than_fred = 6 # Uncle Bob has 6 more
    uncle_bob_candy_bars = fred_candy_bars + bob_more_than_fred

    # L2
    total_fred_bob_candy_bars = fred_candy_bars + uncle_bob_candy_bars

    # L3
    jacqueline_multiplier = 10 # ten times the total number
    jacqueline_candy_bars = jacqueline_multiplier * total_fred_bob_candy_bars

    # L4
    percentage_of_jacqueline_bars = Fraction(40, 100) # 40% of Jacqueline's candy bars
    forty_percent_of_jacqueline_bars = percentage_of_jacqueline_bars * jacqueline_candy_bars

    # FA
    answer = forty_percent_of_jacqueline_bars
    return answer