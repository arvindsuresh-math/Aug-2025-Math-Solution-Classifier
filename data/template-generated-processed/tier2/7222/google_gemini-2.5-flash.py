def solve():
    """Index: 7222.
    Returns: the number of BCM hens.
    """
    # L1
    total_chickens = 100 # 100 chickens
    bcm_percentage_decimal = 0.20 # 20 percent are Black Copper Marans
    num_bcm_chickens = total_chickens * bcm_percentage_decimal

    # L2
    bcm_hens_percentage_decimal = 0.80 # 80 percent of the Black Copper Marans are hens
    num_bcm_hens = num_bcm_chickens * bcm_hens_percentage_decimal

    # FA
    answer = num_bcm_hens
    return answer