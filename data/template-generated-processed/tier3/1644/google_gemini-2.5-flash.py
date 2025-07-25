def solve():
    """Index: 1644.
    Returns: the total amount John spends on memory cards.
    """
    # L1
    years = 3 # for the past 3 years
    days_per_year = 365 # WK
    total_days = years * days_per_year

    # L2
    pictures_per_day = 10 # taken 10 pictures every day
    total_pictures = pictures_per_day * total_days

    # L3
    images_per_card = 50 # each memory card can store 50 images
    memory_cards_needed = total_pictures / images_per_card

    # L4
    cost_per_card = 60 # Each memory card costs $60
    total_cost = memory_cards_needed * cost_per_card

    # FA
    answer = total_cost
    return answer