def solve():
    """Index: 6466.
    Returns: the total expenses for the flowers.
    """
    # L1
    tulips = 250 # 250 tulips
    carnations = 375 # 375 carnations
    roses = 320 # 320 roses
    total_flowers = tulips + carnations + roses

    # L2
    price_per_flower = 2 # Each flower is sold for 2€
    total_expense = total_flowers * price_per_flower

    # FA
    answer = total_expense
    return answer