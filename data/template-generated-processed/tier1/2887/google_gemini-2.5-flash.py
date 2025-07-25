def solve():
    """Index: 2887.
    Returns: Cara's age.
    """
    # L1
    grandmother_age = 75 # Cara's grandmother is 75
    mom_younger_than_grandma = 15 # 15 years younger than Cara's Grandmother
    mom_age = grandmother_age - mom_younger_than_grandma

    # L2
    cara_younger_than_mom = 20 # 20 years younger than her mom
    cara_age = mom_age - cara_younger_than_mom

    # FA
    answer = cara_age
    return answer