def solve():
    """Index: 879.
    Returns: the total number of coins Jake has left.
    """
    # L1
    initial_bitcoin = 80 # Jake amasses a fortune of 80 bitcoin
    first_donation = 20 # He donates 20 bitcoins to charity
    bitcoin_after_first_donation = initial_bitcoin - first_donation

    # L2
    brother_share_divisor = 2 # gives half of all the bitcoins to his brother
    bitcoin_after_brother_share = bitcoin_after_first_donation / brother_share_divisor

    # L3
    tripling_factor = 3 # triples the number of bitcoins he has
    bitcoin_after_tripling = bitcoin_after_brother_share * tripling_factor

    # L4
    second_donation = 10 # donates another 10 coins
    final_bitcoin = bitcoin_after_tripling - second_donation

    # FA
    answer = final_bitcoin
    return answer