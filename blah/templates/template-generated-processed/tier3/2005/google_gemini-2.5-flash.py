def solve():
    """Index: 2005.
    Returns: the total number of cups of lemonade Hazel made.
    """
    # L1
    cups_sold_to_kids = 18 # 18 cups to kids on bikes
    half_divisor = 2 # half that amount
    cups_given_to_friends = cups_sold_to_kids / half_divisor

    # L2
    cups_drank_herself = 1 # drank the last cup of lemonade herself
    total_other_half = cups_sold_to_kids + cups_given_to_friends + cups_drank_herself

    # L3
    cups_sold_to_construction_crew = total_other_half

    # L4
    total_lemonade_made = total_other_half + cups_sold_to_construction_crew

    # FA
    answer = total_lemonade_made
    return answer