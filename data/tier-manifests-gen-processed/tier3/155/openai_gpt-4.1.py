def solve():
    """Index: 155.
    Returns: the number of mangoes Colby still has.
    """
    # L1
    total_kg = 60 # total mangoes he harvested is 60 kilograms
    sold_to_market_kg = 20 # He sold 20 kilograms to the market
    remaining_kg = total_kg - sold_to_market_kg

    # L2
    sold_to_community_fraction_numerator = 1 # sold the remaining half
    sold_to_community_fraction_denominator = 2 # sold the remaining half
    sold_to_community_kg = (sold_to_community_fraction_numerator / sold_to_community_fraction_denominator) * remaining_kg

    # L3
    kg_left = remaining_kg - sold_to_community_kg
    mangoes_per_kg = 8 # each kilogram contains 8 mangoes
    mangoes_left = kg_left * mangoes_per_kg

    # FA
    answer = mangoes_left
    return answer