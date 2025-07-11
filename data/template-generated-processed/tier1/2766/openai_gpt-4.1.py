def solve():
    """Index: 2766.
    Returns: the number of stems of flowers Lara put in the vase.
    """
    # L1
    mom_flowers = 15 # gave 15 flowers to her mom
    more_for_grandma = 6 # gave 6 more flowers than she gave to her mom to her grandma
    grandma_flowers = mom_flowers + more_for_grandma

    # L2
    total_given_away = grandma_flowers + mom_flowers

    # L3
    total_bought = 52 # Lara bought 52 stems of flowers
    in_vase = total_bought - total_given_away

    # FA
    answer = in_vase
    return answer