def solve():
    """Index: 4278.
    Returns: the number of packs of candy Antonov still has.
    """
    # L1
    total_candies_bought = 60 # Antonov bought 60 candies
    candies_in_given_pack = 20 # He gave a pack of candy to his sister. If a pack of candy has 20 pieces
    remaining_candies_pieces = total_candies_bought - candies_in_given_pack

    # L2
    pieces_per_pack = 20 # a pack of candy has 20 pieces
    remaining_packs = remaining_candies_pieces / pieces_per_pack

    # FA
    answer = remaining_packs
    return answer