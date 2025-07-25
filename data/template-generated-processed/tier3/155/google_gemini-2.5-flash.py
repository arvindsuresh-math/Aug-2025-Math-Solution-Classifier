from fractions import Fraction

def solve():
    """Index: 155.
    Returns: the number of mangoes Colby still has.
    """
    # L1
    total_mangoes_kg = 60 # the total mangoes he harvested is 60 kilograms
    sold_to_market_kg = 20 # He sold 20 kilograms to the market
    remaining_after_market_kg = total_mangoes_kg - sold_to_market_kg

    # L2
    community_fraction = Fraction(1, 2) # sold the remaining half to his community
    sold_to_community_kg = community_fraction * remaining_after_market_kg

    # L3
    actual_remaining_kg = remaining_after_market_kg - sold_to_community_kg
    mangoes_per_kg = 8 # If each kilogram contains 8 mangoes
    total_mangoes_pieces = actual_remaining_kg * mangoes_per_kg

    # FA
    answer = total_mangoes_pieces
    return answer