def solve():
    """Index: 7276.
    Returns: the number of bananas in the bowl.
    """
    # L1-L8
    total_fruit_in_bowl = 19 # If the bowl contains 19 pieces of fruit
    pears_more_than_apples = 2 # two more pears than apples
    bananas_more_than_pears = 3 # three more bananas than pears

    # The problem sets up an equation based on the relationships:
    # Let A be the number of apples.
    # Number of pears = A + pears_more_than_apples
    # Number of bananas = (A + pears_more_than_apples) + bananas_more_than_pears
    # Total fruit = Apples + Pears + Bananas
    # total_fruit_in_bowl = A + (A + pears_more_than_apples) + ((A + pears_more_than_apples) + bananas_more_than_pears)
    # total_fruit_in_bowl = 3 * A + 2 * pears_more_than_apples + bananas_more_than_pears
    # Substituting values: 19 = 3 * A + 2 * 2 + 3
    # 19 = 3 * A + 4 + 3
    # 19 = 3 * A + 7
    # 3 * A = 19 - 7
    # 3 * A = 12
    # A = 12 / 3
    num_apples = (total_fruit_in_bowl - (2 * pears_more_than_apples + bananas_more_than_pears)) / 3

    # L9
    num_bananas = (num_apples + pears_more_than_apples) + bananas_more_than_pears

    # FA
    answer = num_bananas
    return answer