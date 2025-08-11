from fractions import Fraction

def solve():
    """Index: 2518.
    Returns: the remaining MB of data Elsa has.
    """
    # L1
    initial_data = 500 # Elsa gets 500 MB of cell phone data each month
    youtube_data = 300 # spends 300 MB watching Youtube
    data_after_youtube = initial_data - youtube_data

    # L2
    facebook_fraction = Fraction(2, 5) # 2/5 of what's left on Facebook
    facebook_data = data_after_youtube * facebook_fraction

    # L3
    remaining_data = data_after_youtube - facebook_data

    # FA
    answer = remaining_data
    return answer