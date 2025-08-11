def solve():
    """Index: 3563.
    Returns: the total number of fruits in the red basket.
    """
    # L1
    bananas_blue_basket = 12 # 12 bananas
    apples_blue_basket = 4 # 4 apples
    total_fruits_blue_basket = bananas_blue_basket + apples_blue_basket

    # L2
    half_divisor = 2 # half as many fruits
    total_fruits_red_basket = total_fruits_blue_basket / half_divisor

    # FA
    answer = total_fruits_red_basket
    return answer