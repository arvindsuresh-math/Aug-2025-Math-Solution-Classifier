def solve():
    """Index: 7140.
    Returns: the height of Marissa's sunflower in feet.
    """
    # L1
    sister_feet_height = 4 # 4 feet 3 inches tall
    inches_per_foot = 12 # 1 foot is equal to 12 inches
    sister_feet_in_inches = sister_feet_height * inches_per_foot

    # L2
    sister_additional_inches = 3 # 4 feet 3 inches tall
    sister_total_inches = sister_feet_in_inches + sister_additional_inches

    # L3
    sunflower_taller_inches = 21 # 21 inches taller
    sunflower_total_inches = sister_total_inches + sunflower_taller_inches

    # L4
    sunflower_total_feet = sunflower_total_inches / inches_per_foot

    # FA
    answer = sunflower_total_feet
    return answer