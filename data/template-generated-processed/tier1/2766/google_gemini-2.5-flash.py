def solve():
    """Index: 2766.
    Returns: the number of stems of flowers Lara put in the vase.
    """
    # L1
    flowers_to_mom = 15 # gave 15 flowers to her mom
    more_flowers_to_grandma = 6 # gave 6 more flowers than she gave to her mom
    flowers_to_grandma = flowers_to_mom + more_flowers_to_grandma

    # L2
    total_given_away = flowers_to_grandma + flowers_to_mom

    # L3
    total_stems_bought = 52 # Lara bought 52 stems of flowers
    flowers_in_vase = total_stems_bought - total_given_away

    # FA
    answer = flowers_in_vase
    return answer