def solve(candy_per_house_anna: int = 14, # pieces of candy per house for Anna
          houses_anna: int = 60,           # number of houses in Anna's subdivision
          candy_per_house_billy: int = 11, # pieces of candy per house for Billy
          houses_billy: int = 75):          # number of houses in Billy's subdivision
    """
    Index: 39.
    Returns: the difference in pieces of candy between Anna and Billy.
    """
    #: L1 Calculate total candy for Anna
    anna_total_candy = candy_per_house_anna * houses_anna

    #: L2 Calculate total candy for Billy
    billy_total_candy = candy_per_house_billy * houses_billy

    #: L3 Calculate the difference in candy
    answer = anna_total_candy - billy_total_candy  # FINAL ANSWER
    return answer