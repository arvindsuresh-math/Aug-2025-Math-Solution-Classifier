def solve():
    """Index: 6335.
    Returns: the number of cucumbers used in the salad.
    """
    # L7
    total_pieces_of_vegetables = 280 # total of 280 pieces of vegetables
    tomatoes_multiplier = 3 # thrice as many tomatoes as cucumbers
    # The problem states c + t = total_pieces_of_vegetables and t = tomatoes_multiplier * c.
    # Substituting t into the first equation gives c + (tomatoes_multiplier * c) = total_pieces_of_vegetables,
    # which simplifies to (1 + tomatoes_multiplier) * c = total_pieces_of_vegetables.
    # The '4' in the solution line L7 is derived from (1 + tomatoes_multiplier).
    coefficient_for_cucumbers = 1 + tomatoes_multiplier
    num_cucumbers = total_pieces_of_vegetables / coefficient_for_cucumbers

    # FA
    answer = num_cucumbers
    return answer