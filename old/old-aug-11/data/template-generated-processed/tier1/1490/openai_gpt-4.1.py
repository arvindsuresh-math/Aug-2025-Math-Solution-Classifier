def solve():
    """Index: 1490.
    Returns: the number of kilograms of strawberries Tommy ordered.
    """
    # L1
    apples_kg = 3 # 3 kilograms of apples
    grapes_kg = 3 # 3 kilograms of grapes
    orange_kg = 1 # 1 kilogram of orange
    non_strawberry_kg = apples_kg + grapes_kg + orange_kg

    # L2
    total_kg = 10 # total weight of 10 kilograms
    strawberries_kg = total_kg - non_strawberry_kg

    # FA
    answer = strawberries_kg
    return answer