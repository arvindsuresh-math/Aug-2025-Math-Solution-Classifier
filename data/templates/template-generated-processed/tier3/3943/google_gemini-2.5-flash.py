from fractions import Fraction

def solve():
    """Index: 3943.
    Returns: the total number of jewelry pieces Jessy has in her box.
    """
    # L1
    initial_necklaces = 10 # 10 necklaces
    initial_earrings = 15 # 15 earrings
    initial_total_jewelry = initial_necklaces + initial_earrings

    # L2
    fraction_bought_earrings = Fraction(2, 3) # 2/3 as many earrings
    earrings_bought_at_store = fraction_bought_earrings * initial_earrings

    # L3
    fraction_from_mother = Fraction(1, 5) # 1/5 times more earrings
    earrings_from_mother = fraction_from_mother * earrings_bought_at_store

    # L4
    total_earrings_received_from_mother = earrings_from_mother + earrings_bought_at_store

    # L5
    total_new_earrings = earrings_bought_at_store + total_earrings_received_from_mother

    # L6
    new_necklaces_bought = 10 # buys 10 more necklaces
    final_total_jewelry = total_new_earrings + new_necklaces_bought + initial_total_jewelry

    # FA
    answer = final_total_jewelry
    return answer